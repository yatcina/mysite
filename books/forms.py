#-*- coding:utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        num_word = len(subject.split())
        if num_word <= 1:
            raise forms.ValidationError("Мало слов")
        return subject
    def clean_message(self):
        message = self.cleaned_data['message']
        num_word = len(message.split())
        if num_word <= 1:
            raise forms.ValidationError("Мало слов")
        return message


