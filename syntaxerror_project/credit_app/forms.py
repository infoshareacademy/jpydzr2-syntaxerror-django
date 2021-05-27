from django import forms


class PredictForm(forms.Form):
    married = forms.ChoiceField(
        required=True,
        choices=((1, "Yes"), (0, "No")),
        label='Are you married?',
    )
    education = forms.ChoiceField(
        required=True,
        choices=((1, "Graduate"), (0, "Not Graduate")),
        label='Your highest academic level',
    )
    applicant_income = forms.IntegerField(
        required=True,
        label='Applicant income',
    )
    co_applicant_income = forms.IntegerField(
        required=True,
        label='Co-applicant income',
    )
    loan_amount = forms.IntegerField(
        required=True,
        label='Loan amount',
    )
    loan_term = forms.IntegerField(
        required=True,
        label='Loan term in months',
    )
    credit_history = forms.ChoiceField(
        required=True,
        choices=((1, "Yes"), (0, "No")),
        label='Do you have a credit history in our bank?',
    )
