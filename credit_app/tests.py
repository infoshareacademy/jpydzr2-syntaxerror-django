from django.test import TestCase, Client
from django.urls import reverse
from django.core.mail import send_mail
from unittest import mock


class ContactTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    @mock.patch('django.core.mail.send_mail')
    def test_contact__negative(self, mail_mock):
        url = reverse('credit_app:submit_prediction')
        data = {'email': 'jakismail@com.com'}
        result = client.post(url, data=data)
        assert not mail_mock.count
    
    @mock.patch('django.core.mail.send_mail')
    def test_contact__negative(self, mail_mock):
        url = reverse('credit_app:submit_prediction')
        data = {'email': 'jakismail@com.com', 'message': 'wiadomość', 'subject': 'tutaj tytuł'}
        result = client.post(url, data=data)
        
        assert mail_mock.count == 1
