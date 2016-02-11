
from django.test import TestCase
from django.core.urlresolvers import reverse


class ContactPageTest(TestCase):
    """
    Test for view contacts
    """

    def test_contacts_page_renders_correct_response(self):
        """
        Contacts view uses correct template for main page
        """
        response = self.client.get(reverse('hello:contacts'))
        self.assertTemplateUsed(response, 'contacts.html')

    def test_contacts_view_get_request(self):
        """
        Check for answer from server
        """
        response = self.client.get(reverse('hello:contacts'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_view_passes_hardcoded_data(self):
        """
        Check for contacts view passes Applicant data to template
        """
        response = self.client.get(reverse('hello:contacts'))

        self.assertEqual(response.context['applicant']['first_name'], 'John')
        self.assertEqual(response.context['applicant']['last_name'], 'Galt')
        self.assertEqual(
            response.context['applicant']['birthday'], '05/02/1879')
        self.assertIn('john.galt@gmail.com', str(response.content))
        self.assertIn('john.galt@khavr.com', str(response.content))
        self.assertIn('Some other contacts', str(response.content))
