from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    telephone = forms.CharField(max_length=30)
    content = forms.CharField(max_length=200)

