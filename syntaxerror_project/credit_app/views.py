import joblib
from django.shortcuts import render
from .forms import PredictForm
from .forms import ContactForm
from .models import PredictModel
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import lightgbm as lgb
from sklearn.preprocessing import MinMaxScaler
from django.views.generic import ListView


# Create your views here.

def predict_and_contact_forms(request):
    if request.method == "POST":
        predict_form = PredictForm(request.POST)
        contact_form = ContactForm(request.POST)

        # handle predict form
        if predict_form.is_valid():
            married = predict_form.cleaned_data['married']
            education = predict_form.cleaned_data['education']
            applicant_income = predict_form.cleaned_data['applicant_income']
            co_applicant_income = predict_form.cleaned_data['co_applicant_income']
            loan_amount = predict_form.cleaned_data['loan_amount']
            loan_term = predict_form.cleaned_data['loan_term']
            credit_history = predict_form.cleaned_data['credit_history']
            total_income = applicant_income + co_applicant_income

            feats = [[married, education, applicant_income,
                      co_applicant_income, loan_amount, loan_term,
                      credit_history, total_income]]

            # Unpickle scaler and scale
            with open('ml_model/MinMaxScaler.save', 'rb') as fo:
                scaler = joblib.load(fo)

            feats_scaled = scaler.transform(feats)

            # Unpickle model
            model = pd.read_pickle('ml_model/LGBM_model.pickle')

            # Make prediction
            result = model.predict_proba(feats_scaled)[:, 1][0]

            if request.user.is_authenticated:
                p = PredictModel(
                    requestor=User.objects.get(username=request.user.username),
                    married=married,
                    education=education,
                    applicant_income=applicant_income,
                    co_applicant_income=co_applicant_income,
                    loan_amount=loan_amount,
                    loan_term=loan_term,
                    credit_history=credit_history,
                    loan_chances=result,
                )
                p.save()

            probability = '{:.2%}'.format(result)
            messages.success(request,
                             'Your chances to get the loan: {}'.format(
                                 probability))

        # handle contact form
        if contact_form.is_valid():
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['m.zajac1988@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    predict_form = PredictForm()
    contact_form = ContactForm()
    return render(request, "index.html", {"predict_form": predict_form, 'contact_form': contact_form})


class RequestsView(LoginRequiredMixin, ListView):
    model = PredictModel
    template_name = 'predictions/loan_requests.html'


def home(request):
    return render(request, 'home.html')


def testimonials(request):
    return render(request, 'testimonials.html')