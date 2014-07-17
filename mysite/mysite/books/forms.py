__author__ = 'Zhanxueyou'
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.clean_message('message')
        num_word = len(message.split())
        if num_word < 4:
            raise forms.ValidationError('No enough words.')
        return message



