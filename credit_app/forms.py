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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if self.user.is_authenticated:
            self.fields['married'].initial = self.user.profile.married
            self.fields['education'].initial = self.user.profile.education
        self.fields['loan_term'].initial = 360

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)