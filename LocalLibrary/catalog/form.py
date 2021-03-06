from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
    renewal_data = forms.DateField(help_text="Enter a date between now and 4 weeks (Default 3 weeks).")

    def clean_renewal_data(self):
        data = self.cleaned_data['renewal_data']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data