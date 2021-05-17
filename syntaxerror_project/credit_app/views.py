import joblib
from django.shortcuts import render, redirect
from credit_app.forms import PredictForm
from django.contrib import messages
from django.http import JsonResponse
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
            probability = '{:.2%}'.format(result)
            messages.success(request, 'Your chances to get the loan: {}'.format(probability))

    form = PredictForm()
    return render(request, "predict.html", {"form": form})

# def predict_chances(request):
#     if request.POST.get('action') == 'post':
#         # Receive data from client
#         married = str(request.POST.get('married'))
#         education = str(request.POST.get('education'))
#         applicant_income = float(request.POST.get('applicant_income'))
#         co_applicant_income = float(request.POST.get('co_applicant_income'))
#         loan_amount = float(request.POST.get('loan_amount'))
#         loan_term = float(request.POST.get('loan_term'))
#         credit_history = str(request.POST.get('credit_history'))
#         total_income = applicant_income + co_applicant_income
#
#         married = 1 if married == 'True' else 0
#         credit_history = 1 if credit_history == 'True' else 0
#         education = 1 if education == 'Graduate' else 0
#
#         feats = [[married, education, applicant_income,
#                   co_applicant_income, loan_amount, loan_term,
#                   credit_history, total_income]]
#
#         # Unpickle scaler and scale
#         with open('ml_model/MinMaxScaler.save', 'rb') as fo:
#             scaler = joblib.load(fo)
#
#         feats_scaled = scaler.transform(feats)
#
#         # Unpickle model
#         model = pd.read_pickle('ml_model/LGBM_model.pickle')
#
#         # Make prediction
#         result = model.predict_proba(feats_scaled)[:, 1][0]
#
#         probability = '{:.2%}'.format(result)
#
#         # PredResults.objects.create(married=married, education=education, applicant_income=applicant_income,
#         #                            co_applicant_income=co_applicant_income, loan_amount=loan_amount,
#         #                            loan_term=loan_term, credit_history=credit_history, probability=probability)
#
#         return JsonResponse(
#             {'probability': probability,
#              'loan_amount': loan_amount,
#              'loan_term': loan_term,
#              'applicant_income': applicant_income,
#              'co_applicant_income': co_applicant_income},
#             safe=False)
