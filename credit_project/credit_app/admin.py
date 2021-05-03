from django.contrib import admin

# Register your models here.
from credit_app.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = [
    'gender',
    'married',
    'dependents',
    'education',
    'self_employed',
    'applicant_income',
    'coapplicant_income',
    'loan_amount',
    'loan_amount_term',
    'credit_history',
    'property_area',


    ]