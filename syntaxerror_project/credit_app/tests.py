from django.test import TestCase
from django.http import JsonResponse
from django.test.client import Client

# Create your tests here.

from django.urls import reverse


class PredictionTestCase(TestCase):

    def setUp(self):

        self.client =  Client()

    def test_get_probabilty__positive(self):


        data = {
            'married': 'True',
            'education': 'True',
            'applicant_income': 1000,
            'co_applicant_income': 3000,
            'loan_amount': 10,
            'loan_term': 12,
            'credit_history': 'True',
            'action':'post',

        }
        url = reverse('credit_app:submit_prediction')
        response = self.client.post(url, data=data)
        self.assertIsInstance(response,JsonResponse)