from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Loan_ID--------------> Unique Loan ID.
# Gender --------------> Male/ Female
# Married --------------> Applicant married (Y/N)
# Dependents ------------> Number of dependents
# Education -------------> Applicant Education (Graduate/ Under Graduate)
# Self_Employed ---------> Self-employed (Y/N)
# ApplicantIncome -------> Applicant income
# CoapplicantIncome -----> Coapplicant income
# LoanAmount -----------> Loan amount in thousands
# Loan_Amount_Term ------> Term of a loan in months
# Credit_History --------> Credit history meets guidelines
# Property_Area ---------> Urban/ Semi-Urban/ Rural
# Loan_Status -----------> Loan approved (Y/N)


class Credit(models.Model):
    gender = models.CharField('gender', max_length=6, blank=False, null=False)
    married = models.BinaryField('married', max_length=6, blank=False, null=False)
    dependents = models.IntegerField('Dependents', blank=False, null=False)
    education = models.CharField('Education', max_length=25, blank=False, null=False)
    self_employed = models.BinaryField('Self_Employed', max_length=6, blank=False, null=False)
    applicant_income = models.IntegerField('ApplicantIncome', blank=False, null=False)
    coapplicant_income = models.IntegerField('CoapplicantIncome', blank=False, null=False)
    loan_amount = models.IntegerField('LoanAmount', blank=False, null=False)
    loan_amount_term = models.IntegerField('Loan_Amount_Term', blank=False, null=False)
    credit_history = models.CharField('Credit_History', max_length=6, blank=False, null=False)
    property_area = models.CharField('Property_Area', max_length=6, blank=False, null=False)



