
from django.shortcuts import render

# Create your views here.


def contacts(request):
    """
    View for main page
    """

    applicant = {
            'first_name': 'John',
            'last_name': 'Galt',
            'email': 'john.galt@gmail.com',
            'jabber': 'john.galt@khavr.com',
            'skype': 'john.galt',
            'birthday': '05/02/1879',
            'bio': 'Some bio',
            'contacts': 'Some other contacts'
    }

    return render(request, 'contacts.html', {'applicant': applicant})
