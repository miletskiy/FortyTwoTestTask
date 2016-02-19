
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
import json

# Create your views here.
from .models import Applicant
from .models import DatabaseRequest
from .forms import ApplicantForm

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
    requests = DatabaseRequest.objects.all()[:10]

    if request.is_ajax():
        data = serializers.serialize('json', requests)
        return HttpResponse(data, content_type='application/json')

    return render(request, 'requests_list.html', {'requests': requests})


def edit_applicant(request):
    """
    View for edit data page
    """
    applicant = Applicant.objects.first()

    if request.method == 'POST':
        form=ApplicantForm(request.POST, request.FILES, instance=applicant)
        if request.POST.get('save_button') is not None:
            if form.is_valid():
                form.save()
                if request.is_ajax():
                    # print 'AJAXform is valid'
                    return HttpResponse(json.dumps('Success'),
                                        content_type="application/json")
                else:
                    pass
                    # print 'Just valid form'

            else:
                if request.is_ajax():
                    # print 'invalid AJAXform+++++++++==========='
                    print form.errors
                    return HttpResponseBadRequest(json.dumps(form.errors),
                                            content_type='application/json')
                else:
                    pass
                    # print 'invalid form without AJAX ---------'
    else:
        form = ApplicantForm(instance=applicant)

    return render(request, 'edit_applicant.html', {'form':form})
