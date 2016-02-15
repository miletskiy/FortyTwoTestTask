
from django.shortcuts import render

# Create your views here.
from .models import Applicant


def contacts(request):
    """
    View for main page
    """

    applicant = Applicant.objects.first()

    return render(request, 'contacts.html', {'applicant': applicant})


def requests_list(request):
    """
    View for requests page
    """

    return render(request, 'requests_list.html')
