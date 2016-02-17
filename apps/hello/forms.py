
from django.forms import ModelForm

from .models import Applicant


class ApplicantForm(forms.ModelForm):
    """
    Form for edit Applicant instance
    """

    class Meta:
        model = Applicant
        fields = ('',)
