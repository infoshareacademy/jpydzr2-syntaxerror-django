import joblib
from django.shortcuts import render
from credit_app.forms import PredictForm
from credit_app.models import PredictModel
from django.contrib.auth.models import User
from django.contrib import messages
import pandas as pd
import lightgbm as lgb
from sklearn.preprocessing import MinMaxScaler


# Create your views here.

def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            married = form.cleaned_data['married']
            education = form.cleaned_data['education']
            applicant_income = form.cleaned_data['applicant_income']
            co_applicant_income = form.cleaned_data['co_applicant_income']
            loan_amount = form.cleaned_data['loan_amount']
            loan_term = form.cleaned_data['loan_term']
            credit_history = form.cleaned_data['credit_history']
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
                    married=married, education=education,
                    applicant_income=applicant_income,
                    co_applicant_income=co_applicant_income,
                    loan_amount=loan_amount, loan_term=loan_term,
                    credit_history=credit_history, loan_chances=result,
                )
                p.save()

            probability = '{:.2%}'.format(result)
            messages.success(request,
                             'Your chances to get the loan: {}'.format(
                                 probability))

    form = PredictForm()
    return render(request, "predict.html", {"form": form})