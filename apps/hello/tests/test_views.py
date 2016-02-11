
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

