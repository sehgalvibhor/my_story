from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, required=True)
    gmail_id = forms.EmailField(label='Gmail ID',required=True)
    gmail_pass = forms.CharField(widget=forms.PasswordInput,required=True,label='Password')