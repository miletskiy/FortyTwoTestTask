
from django.shortcuts import render

# Create your views here.
from .models import Applicant
import datetime


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
    requests = []
    for i in range(10):
        loq = request.GET.copy()
        loq['time'] = datetime.datetime.now()
        request.GET = loq
        requests.append(request)

    return render(request, 'requests_list.html', {'requests': requests})
