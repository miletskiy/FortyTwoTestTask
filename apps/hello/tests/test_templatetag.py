
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Applicant
from ..templatetags.admin_tag import edit_link


class TemplateTagAdminTest(TestCase):
    """
    Test for template tag that accepts any object
    and renders the link to its admin edit page
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.home_url = reverse('hello:contacts')

    def test_page_contains_link_to_admin_edit_page(self):
        """
        Custom admin tag converted to admin edit object link
        """
        self.client.login(username='admin', password = 'admin')
        response = self.client.get(self.home_url)
        applicant = Applicant.objects.first()
        tag_link = edit_link(applicant)
        anyobject = applicant
        super_link = '{0}{1}/{2}/{3}/'.format( reverse('admin:index'),
                                                anyobject._meta.app_lable,
                                                anyobject._meta.model,
                                                anyobject.pk )

        sefl.assertIn(super_link, response.content)
        self.assertEqual(tag_link, super_link)