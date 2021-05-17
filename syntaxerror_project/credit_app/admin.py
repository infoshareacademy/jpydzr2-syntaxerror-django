from django.contrib import admin
from credit_app.models import PredictModel


# Register your models here.

@admin.register(PredictModel)
class PredictModelAdmin(admin.ModelAdmin):

    list_display = [
        '__str__',
        'married',
        'education',
        'applicant_income',
        'co_applicant_income',
        'loan_amount',
        'loan_term',
        'credit_history',
        'loan_chances',
    ]
