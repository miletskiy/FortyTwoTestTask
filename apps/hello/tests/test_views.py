
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from ..models import Applicant


class ContactPageTest(TestCase):
    """
    Test for view contacts
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.home_url = reverse('hello:contacts')

    def test_contacts_view(self):
        """
        Contacts view uses correct template for main page,
        answer from server and uses correct instance in the template
        """
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'contacts.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['applicant'], Applicant)

    def test_contacts_view_passes_correct_insatance(self):
        """
        Check the view passes correct instance to the main template
        """
        Applicant.objects.create(
            first_name='John',
            last_name='Galt',
            email='john.galt@gmail.com',
            jabber='john.galt@khavr.com',
            skype='john.galt',
            birthday='1879-02-05',
            bio='Some bio',
            contacts='Some other contacts'
            )
        applicant1 = Applicant.objects.first()
        applicant2 = Applicant.objects.last()
        applicants = Applicant.objects.all().count()

        response = self.client.get(self.home_url)

        self.assertEqual(applicants, 2)
        self.assertEqual(response.context['applicant'], applicant1)
        self.assertNotEqual(response.context['applicant'], applicant2)

    def test_database_is_empty(self):
        """"
        Check that database not contains objects.
        """
        applicants = Applicant.objects.all().delete()
        applicants = Applicant.objects.all().count()
        response = self.client.get(self.home_url)

        self.assertEqual(applicants, 0)
        self.assertIsNone(response.context['applicant'])
        self.assertIn('There are no applicants in database.', response.content)


class RequestsPageTest(TestCase):
    """
    Test for requests view
    """

    def setUp(self):
        self.requests_url = reverse('hello:requests')

    def test_requests_view_returning_hardcoded_data_for_the_template(self):
        """
        Requests view uses correct template for requests page,
        get answer from server and passes 10 objects
        """
        response = self.client.get(self.requests_url)
        length_requests = len(response.context['requests'])

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests_list.html')
        self.assertEqual(length_requests, 10)
        self.assertIsInstance(response.context['requests'][0], HttpRequest)
