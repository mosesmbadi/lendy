
# Loan Management System
This is a Django-based Loan Management System designed to handle loan applications, scoring engine integration, and core banking system interactions. The system is built using Django Rest Framework (DRF) for the API layer and Celery for asynchronous task management.
It includes a SOAP client for interacting with external services and is structured to allow for easy integration with other systems.



## Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [User Journey](#user-journey)
- [API Examples](#api-examples)
- [Potential Issues](#potential-issues)
- [How to Run](#how-to-run)
  - [Using Docker](#with-docker)
  - [Without Docker](#without-docker)
- [License](#license)


## Features
- **Loan Application Management**: Create, update, and manage loan applications.
- **Scoring Engine Integration**: Interface with a scoring engine to evaluate loan applications.
- **Core Banking System Integration**: Connect with a core banking system for loan processing.
- **Asynchronous Processing**: Use Celery for background tasks, such as sending notifications or processing applications.
- **SOAP Client**: Interact with external SOAP APIs for additional services.
- **Custom Permissions**: Implement custom permissions for API access.
- **DRF Serializers**: Use Django Rest Framework serializers for data validation and transformation.
- **Unit Tests**: Comprehensive unit tests for all modules to ensure reliability and maintainability.

## System Architecture
The system is designed with a modular architecture to separate concerns and facilitate easier maintenance and scalability. The main components include:
The project is broken down into the modules below:
kopa/
    ├── loan_app/          ====> Main application for loan management
    │   ├── models.py      ====> Database models
    │   ├── serializers.py ====> DRF serializers for data conversion
    │   ├── views.py        ====> DRF viewsets for API logic
    │   ├── urls.py         ====> API routing
    │   ├── permissions.py  ====> Custom permissions (if needed)
    │   ├── services.py     ====> Business logic services
    │   ├── tasks.py        ====> Celery tasks for async operations (e.g., retries)
    │   └── soap_client.py  ====> For interacting with SOAP APIs
    ├── scoring_engine_integration/ ====>For interacting with Scoring Engine
    │   ├── services.py
    ├── core_banking_integration/ ====>For interacting with CORE Banking System
    │   ├── services.py
    ├── config/           ====> Project-level settings
    │   ├── settings.py
    │   ├── urls.py       ====> Project-level URL routing
    │   └── celery.py     ====> Celery configuration
    └── manage.py         ====> Django management script


## User Journey
- Bank sends customer pin to register
- Bank submits loan request
- LMS queries score
- LMS Registers with Scoring platform
- Scoring Platform registers with LMS
- Scoring Platform queries transaction data

### Bank sends customer pin to register
curl --request POST \
  --url http://127.0.0.1:8000/customers/ \
  --header 'Authorization: Bearer {access_token}' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
 "customer_number": "234774784",
 "name": "John Doe",
 "address": "123 Main St",
 "other_kyc_data": "..."
}'

### Bank submits loan request
curl --request POST \
  --url http://127.0.0.1:8000/loans/ \
  --header 'Authorization: Bearer {access_token}' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.6.1' \
  --data '{
 "customer_number": "234774784",
 "amount": 2000.00
}'

  #### LMS queries KYC
  core_banking_service = CoreBankingService()
  customer_data = core_banking_service.get_customer_kyc(customer_number)
  ### Loan is Created
  ### Calls scoring API 
  --> The loan object is updated with the scoring token
  ### Asynchronous Scoring
  --> A Celery task is triggered to fetch the loan score and limit



## Potential Issues
If the Core Banking API is down, loan creation will fail.

If Scoring Engine API fails, the loan is still created, but scoring is delayed.

If the Celery worker isn't running, loan scores won't be retrieved automatically.

# How to run
## With Docker
This is the most straightforward way to run the project. 
Just rename .env.sample to .env then type docker compose up
You must have docker and dockerc ompose installed
You can then exec into the container and run the migrations
```bash
docker exec -it lms bash
```
Then run the migrations
```bash
python manage.py migrate
```
Create a superuser
```bash
python manage.py createsuperuser
```

## Without Docker
Make sure you have virtualenv installed
```bash
pip install virtualenv
```
Create a virtual environment
```bash
virtualenv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```
Install the required packages
```bash
pip install -r requirements.txt
```
Run the migrations
```bash
python manage.py migrate
```
Create a superuser
```bash
python manage.py createsuperuser
```
Run the server
```bash
python manage.py runserver
```
