from loan_app.models import Loan
# from .tasks import get_score_and_limit_task
from rest_framework import status
from rest_framework.response import Response
import requests
from django.conf import settings
import time
from celery import shared_task


class ScoringEngineService:
      # The base URL for the scoring engine service
    SCORING_ENGINE_BASE_URL = 'rabbitmq:2323'
      #  Call Scoring Engine - Step 1
    CLIENT_BASE_URL = 'https://scoringtest.credable.io/api/v1/client'


def initiate_query_score(self, customer_number):
    #  Call Scoring Engine - Step 1
    url = (
    f'{self.SCORING_ENGINE_BASE_URL}/initiateQueryScore/{customer_number}'
    )
    headers = {'client-token': settings.SCORING_ENGINE_CLIENT_TOKEN} #TODO: get from DB
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    return response.text.strip('"')  # Extract the token


@shared_task(bind=True, max_retries=5)
def get_score_and_limit_with_retry(self, loan_id, token):
    #  Call Scoring Engine - Step 2 with retries
    try:
        loan = Loan.objects.get(id=loan_id)
        url = f'{self.SCORING_ENGINE_BASE_URL}/queryScore/{token}'
        headers = {'client-token': settings.SCORING_ENGINE_CLIENT_TOKEN} #TODO: get from DB
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        loan.loan_score = data['score']
        loan.limit_amount = data['limitAmount']
        loan.status = 'APPROVED'
        loan.save()
    except requests.exceptions.RequestException as exc:
        #  Retry the task
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)
    except Loan.DoesNotExist:
        #  Log an error or handle the case where the loan is deleted
        print(f'Loan with id {loan_id} not found.')
    except self.max_retries:
        loan.status = 'FAILED'
        loan.save()
        print('Max retries reached. Loan application failed.')


def register_client(self, url, name, username, password):
    #  Call the client registration API
    registration_url = f'{self.CLIENT_BASE_URL}/createClient'
    payload = {
    'url': url,
    'name': name,
    'username': username,
    'password': password,
    }
    response = requests.post(registration_url, json=payload)
    response.raise_for_status()
    return response.json()
