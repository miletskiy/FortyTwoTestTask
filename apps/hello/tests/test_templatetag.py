
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Context, Template

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
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.home_url)
        applicant = Applicant.objects.first()
        tag_link = edit_link(applicant)
        anyobject = applicant
        super_link = '{0}{1}/{2}/{3}/'.format(reverse('admin:index'),
                                              anyobject._meta.app_label,
                                              anyobject._meta.model_name,
                                              anyobject.pk)

        self.assertIn(super_link, response.content)
        self.assertEqual(tag_link, super_link)

    def test_presents_in_the_template(self):
        """
        Custom admin tag presents in the template
        """
        applicant = Applicant.objects.first()
        anyobject = applicant
        super_link = '{0}{1}/{2}/{3}/'.format(reverse('admin:index'),
                                              anyobject._meta.app_label,
                                              anyobject._meta.model_name,
                                              anyobject.pk)
        template_tag = '{% load admin_tag %}{% edit_link applicant %}'
        template = Template(template_tag)
        context = Context({'applicant': applicant})

        self.assertEqual(super_link, template.render(context))

    def test_tag_accepts_NOT_model_instance(self):
        """
        Custom admin tag get not model instance
        and redirects to main page
        """
        anyobject = 'anyobject'
        tag_link = edit_link('anyobject')

        self.assertEqual(tag_link, self.home_url)
