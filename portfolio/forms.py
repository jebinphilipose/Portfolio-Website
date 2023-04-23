from django import forms

from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'validate',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'validate',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'validate materialize-textarea',
    }))
    captcha = ReCaptchaField()
