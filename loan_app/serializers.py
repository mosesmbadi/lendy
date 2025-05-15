from rest_framework import serializers
from .models import Customer, Loan, Repayment


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    

class LoanRequestSerializer(serializers.Serializer):
    customer_number = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class LoanSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = '__all__'
    

class TransactionDataSerializer(serializers.Serializer):
    accountNumber = serializers.CharField()
    alternativechanneltrnscrAmount = serializers.FloatField()
    alternativechanneltrnscrNumber = serializers.IntegerField()
    alternativechanneltrnsdebitAmount = serializers.FloatField()
    alternativechanneltrnsdebitNumber = serializers.IntegerField()
    atmTransactionsNumber = serializers.IntegerField()
    atmtransactionsAmount = serializers.FloatField()
    bouncedChequesDebitNumber = serializers.IntegerField()
    bouncedchequescreditNumber = serializers.IntegerField()
    bouncedchequetransactionscrAmount = serializers.FloatField()
    bouncedchequetransactionsdrAmount = serializers.FloatField()
    chequeDebitTransactionsAmount = serializers.FloatField()
    chequeDebitTransactionsNumber = serializers.IntegerField()
    createdAt = serializers.IntegerField()
    createdDate = serializers.IntegerField()
    credittransactionsAmount = serializers.FloatField()
    debitcardpostransactionsAmount = serializers.FloatField()
    debitcardpostransactionsNumber = serializers.IntegerField()
    fincominglocaltransactioncrAmount = serializers.FloatField()
    id = serializers.IntegerField()
    incominginternationaltrncrAmount = serializers.FloatField()
    incominginternationaltrncrNumber = serializers.IntegerField()
    incominglocaltransactioncrNumber = serializers.IntegerField()
    intrestAmount = serializers.IntegerField()
    lastTransactionDate = serializers.IntegerField()
    lastTransactionType = serializers.CharField(allow_null=True)
    lastTransactionValue = serializers.IntegerField()
    maxAtmTransactions = serializers.FloatField()
    maxMonthlyBebitTransactions = serializers.FloatField()
    maxalternativechanneltrnscr = serializers.FloatField()
    maxalternativechanneltrnsdebit = serializers.FloatField()
    maxbouncedchequetransactionscr = serializers.FloatField()
    maxchequedebittransactions = serializers.FloatField()
    maxdebitcardpostransactions = serializers.FloatField()
    maxincominginternationaltrncr = serializers.FloatField()
    maxincominglocaltransactioncr = serializers.FloatField()
    maxmobilemoneycredittrn = serializers.FloatField()
    maxmobilemoneydebittransaction = serializers.FloatField()
    maxmonthlycredittransactions = serializers.FloatField()
    maxoutgoinginttrndebit = serializers.FloatField()
    maxoutgoinglocaltrndebit = serializers.FloatField()
    maxoverthecounterwithdrawals = serializers.FloatField()
    minAtmTransactions = serializers.FloatField()
    minMonthlyDebitTransactions = serializers.FloatField()
    minalternativechanneltrnscr = serializers.FloatField()
    minalternativechanneltrnsdebit = serializers.FloatField()
    minbouncedchequetransactionscr = serializers.FloatField()
    minchequedebittransactions = serializers.FloatField()
    mindebitcardpostransactions = serializers.FloatField()
    minincominginternationaltrncr = serializers.FloatField()
    minincominglocaltransactioncr = serializers.FloatField()
    minmobilemoneycredittrn = serializers.FloatField()
    minmobilemoneydebittransaction = serializers.FloatField()
    minmonthlycredittransactions = serializers.FloatField()
    minoutgoinginttrndebit = serializers.FloatField()
    minoutgoinglocaltrndebit = serializers.FloatField()
    minoverthecounterwithdrawals = serializers.FloatField()
    mobilemoneycredittransactionAmount = serializers.FloatField()
    mobilemoneycredittransactionNumber = serializers.IntegerField()
    mobilemoneydebittransactionAmount = serializers.FloatField()
    mobilemoneydebittransactionNumber = serializers.IntegerField()
    monthlyBalance = serializers.FloatField()
    monthlydebittransactionsAmount = serializers.FloatField()
    outgoinginttransactiondebitAmount = serializers.FloatField()
    outgoinginttrndebitNumber = serializers.IntegerField()
    outgoinglocaltransactiondebitAmount = serializers.FloatField()
    outgoinglocaltransactiondebitNumber = serializers.IntegerField()
    overdraftLimit = serializers.FloatField()
    overthecounterwithdrawalsAmount = serializers.FloatField()
    overthecounterwithdrawalsNumber = serializers.IntegerField()
    transactionValue = serializers.FloatField()
    updatedAt = serializers.IntegerField()
    

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'