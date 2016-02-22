
from django import forms
from django.forms import Textarea

from .models import Applicant
from .widgets import CustomCalendarWidget


class ApplicantForm(forms.ModelForm):
    """
    Form for edit Applicant instance
    """

    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name', 'birthday', 'bio',
                  'email', 'jabber', 'skype', 'contacts', 'photo')
        widgets = {
            'contacts': Textarea(attrs={'cols': 60, 'rows': 3}),
            'bio': Textarea(attrs={'cols': 60, 'rows': 16}),
            'birthday': CustomCalendarWidget()
        }
