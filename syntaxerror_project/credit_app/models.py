from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class PredictModel(models.Model):
    requestor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    married = models.IntegerField()
    education = models.IntegerField()
    applicant_income = models.IntegerField()
    co_applicant_income = models.IntegerField()
    loan_amount = models.IntegerField()
    loan_term = models.IntegerField()
    credit_history = models.IntegerField()
    loan_chances = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return '{}'.format(self.requestor)

