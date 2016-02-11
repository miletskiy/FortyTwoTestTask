
from django.shortcuts import render

# Create your views here.


def contacts(request):
    """
    View for main page
    """
    return render(request, 'contacts.html')
