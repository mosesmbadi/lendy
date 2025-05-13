from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Loan, Repayment
from .serializers import (
CustomerSerializer,
LoanRequestSerializer,
LoanSerializer,
TransactionDataSerializer,
RepaymentSerializer,
)
from .services import (
    CoreBankingService,
    ScoringEngineService,
    LoanService,
    TransactionDataService,
    )
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    # A Loan request will go through 3 stages
    # 1. Check for Pending Loans
    # 2. Fecth KYC
    # 3. Initiate Scoring
    # 4. Asynchronously get the score and limit with retries
    # All handled by LoanService()
    def create(self, request, *args, **kwargs):
        serializer = LoanRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_number = serializer.validated_data['customer_number']
        amount = serializer.validated_data['amount']

        loan_service = LoanService()
        try:
            loan = loan_service.create_loan(customer_number, amount)
            return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def status(self, request):
        customer_number = request.query_params.get('customer_number')
        if not customer_number:
            return Response(
                {'error': 'customer_number is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        loan_service = LoanService()
        loan_status = loan_service.get_loan_status(customer_number)
        return Response({'status': loan_status})
    

class TransactionDataView(views.APIView):

    def post(self, request):
        serializer = TransactionDataSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(
        {'message': 'Transaction data received'}, status=status.HTTP_200_OK
        )
        
        
class RepaymentViewSet(ModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated]
