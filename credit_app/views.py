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
from django.conf import settings

# Create your views here.

def _get_probability(clean_data):
    total_income = clean_data['applicant_income'] + clean_data['co_applicant_income']

    feats = [[key for key in clean_data.keys()]]
    feats[0].append(total_income)

    with open('ml_model/MinMaxScaler.save', 'rb') as fo:
        scaler = joblib.load(fo)

    feats_scaled = scaler.transform(feats)

    model = pd.read_pickle('ml_model/LGBM_model.pickle')

    return model.predict_proba(feats_scaled)[:, 1][0]

def _send_contact_form_email(clean_data):
    email = clean_data['email']
    subject = clean_data['subject']
    message = clean_data['message']

    try:
        send_mail(subject, message, email, ['m.zajac1988@gmail.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def predict_and_contact_forms(request):
    if request.method == "POST":
        predict_form = PredictForm(request.POST)
        contact_form = ContactForm(request.POST)

        if predict_form.is_valid():
            result = _get_probability(predict_form.cleaned_data)

            if request.user.is_authenticated:
                p = PredictModel(
                    requestor=User.objects.get(username=request.user.username),
                    loan_chances=result,
                    **predict_form.cleaned_data
                )
                p.save()

            probability = '{:.2%}'.format(result)
            messages.success(request,
                             'Your chances to get the loan: {}'.format(
                                 probability))

        if contact_form.is_valid():
            _send_contact_form_email(predict_form.cleaned_data)

    return render(request, "index.html", {"predict_form": PredictForm(),
                                          'contact_form': ContactForm(),
                                          'api_key': settings.GOOGLE_MAPS_API_KEY})


class RequestsView(LoginRequiredMixin, ListView):
    model = PredictModel
    template_name = 'predictions/loan_requests.html'


def home(request):
    return render(request, 'home.html')


def testimonials(request):
    return render(request, 'testimonials.html')