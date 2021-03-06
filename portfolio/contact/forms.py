from django import forms
from django.urls import reverse
from .models import ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        exclude = ['submitted_date']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contactForm'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact')