
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Applicant
from .models import DatabaseRequest
from .forms import ApplicantForm
from .signals import save_to_db_changes_of_objects_signal  # noqa


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
    requests = DatabaseRequest.objects.all()
    order_by = request.GET.get('order_by', '')

    if order_by == 'priority':
        requests = requests.order_by(order_by, '-emergence')
        if request.GET.get('reverse', '') == 'true':
            requests = requests.order_by('-priority', '-emergence')

    requests = requests[:10]

    if request.is_ajax():
        data = serializers.serialize('json', requests)
        return HttpResponse(data, content_type='application/json')

    return render(request, 'requests_list.html', {'requests': requests})


@login_required
def edit_applicant(request):
    """
    View for edit data page
    """
    applicant = Applicant.objects.first()

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES, instance=applicant)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                data = {}
                data['link_file'] = applicant.photo.name or None
                return HttpResponse(json.dumps(data),
                                    content_type="application/json")
        else:
            if request.is_ajax():
                return HttpResponse(json.dumps(form.errors),
                                    content_type='application/json')
    else:
        form = ApplicantForm(instance=applicant)

    return render(request, 'edit_applicant.html', {'form': form})
