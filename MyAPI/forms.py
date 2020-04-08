from django.forms import ModelForm
from . models import approvals


class MyForm(ModelForm):
    class Meta:
        model = approvals
        fields = '__all__'
        #exclude = 'firstname'

# from django import forms


# class ApprovalForm(forms.Form):

#     firstname = forms.CharField(max_length=15)
#     lastname = forms.CharField(max_length=15)
#     dependants = forms.IntegerField()
#     applicantincome = forms.IntegerField()
#     coapplicatincome = forms.IntegerField()
#     loanamt = forms.IntegerField()
#     loanterm = forms.IntegerField()
#     credithistory = forms.IntegerField()
#     gender = forms.ChoiceField(
#         Choices=[('Male', 'Maek'), ('Female', 'Female')])
#     married = forms.ChoiceField(Choices=[(('Yes', 'Yes'), ('No', 'No'))])
#     graduatededucation = forms.ChoiceField(Choices=[(
#         ('Graduate', 'Graduated'),
#         ('Not_Graduate', 'Not_Graduate')
#     )])
#     selfemployed = forms.ChoiceField(Choices=[(
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )])
#     area = forms.ChoiceField(Choices=[(
#         ('Rural', 'Rural'),
#         ('Semiurban', 'Semiurban'),
#         ('Urban', 'Urban')
#     )])
