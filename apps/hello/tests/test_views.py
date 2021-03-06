
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db.models import ImageField

from ..models import Applicant
from ..models import DatabaseRequest
from ..forms import ApplicantForm


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
        applicant = Applicant.objects.first()
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'contacts.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['applicant'], Applicant)
        self.assertEqual(response.context['applicant'].first_name,
                         applicant.first_name)
        self.assertEqual(response.context['applicant'].last_name,
                         applicant.last_name)
        self.assertEqual(response.context['applicant'].email,
                         applicant.email)
        self.assertEqual(response.context['applicant'].birthday,
                         applicant.birthday)
        self.assertEqual(response.context['applicant'].bio,
                         applicant.bio)

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
        Applicant.objects.all().delete()
        applicants = Applicant.objects.all().count()
        response = self.client.get(self.home_url)

        self.assertEqual(applicants, 0)
        self.assertIsNone(response.context['applicant'])
        self.assertIn('There are no applicants in database.', response.content)

    def test_applicatn_have_image_field(self):
        """
        Check that applicant instance have ImageField
        """
        field_photo = Applicant._meta.get_field('photo')

        self.assertIsInstance(field_photo, ImageField)

    def test_resizing_applicant_image(self):
        """
        Check that applicant image resizing to 200x200 px
        """
        from PIL import Image
        from StringIO import StringIO
        from django.core.files.base import ContentFile

        image_file = StringIO()
        image = Image.new('RGBA', size=(420, 420), color=(256, 0, 0))
        image.save(image_file, 'png')
        image_file.seek(0)
        django_friendly_file = ContentFile(image_file.read(), 'test.png')

        applicant = Applicant.objects.first()
        self.assertFalse(applicant.photo)
        applicant.photo = django_friendly_file
        applicant.save()
        applicant = Applicant.objects.first()

        self.assertTrue(applicant.photo)
        self.assertEqual(applicant.photo.width, 200)
        self.assertEqual(applicant.photo.height, 200)


class RequestsPageTest(TestCase):
    """
    Test for requests view
    """

    def setUp(self):
        self.requests_url = reverse('hello:requests')

    def test_requests_view_is_alive(self):
        """
        Requests view uses correct template for requests page,
        get answer from server and passes 10 objects
        """
        self.client.get(reverse('hello:contacts'))
        response = self.client.get(self.requests_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests_list.html')
        self.assertIsInstance(response.context['requests'][0], DatabaseRequest)

    def test_requests_view_passes_10_objects(self):
        """
        Requests view passes exactly 10 objects
        and view passes objects in right order
        """
        for i in range(15):
            self.client.get(reverse('hello:contacts'))
        response = self.client.get(self.requests_url)
        quantity_requests = DatabaseRequest.objects.all().count()
        length_requests = len(response.context['requests'])
        first_request = DatabaseRequest.objects.first()

        self.assertEqual(length_requests, 10)
        self.assertEqual(quantity_requests, 15)
        self.assertEqual(first_request.pk, 15)

    def test_asynchronously_udates_requests_page(self):
        """Requests page should updates asynchronously
            as new requests come in
        """
        self.client.get(reverse('hello:contacts'))
        responseAJAX = self.client.get(reverse('hello:requests'),
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertContains(responseAJAX, '"pk": 1', 1, 200)

        self.client.get(reverse('hello:contacts'))
        responseAJAX = self.client.get(reverse('hello:requests'),
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertContains(responseAJAX, '"pk": 2', 1, 200)

    def test_if_not_middleware_database_empty(self):
        """
        Check if the middleware is absent or not working,
        there are no DatabaseRequest records in the database
        """
        quantity_reqs = DatabaseRequest.objects.all().count()
        self.assertEqual(quantity_reqs, 0)

        responseAJAX = self.client.get(reverse('hello:requests'),
                                       HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(len(responseAJAX.content), 2)


class EditApplicantPageTest(TestCase):
    """
    Test for edit_applicant view
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.edit_url = reverse('hello:edit_applicant')

    def test_edit_applicant_page_redirects_for_anonymous_user(self):
        """
        Check that edit_applicant redirects for anonymous user
        """
        response = self.client.get(reverse('hello:edit_applicant'))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.content)

    def test_edit_applicant_view_is_alive(self):
        """
        Edit_applicant view uses correct template for edit_applicant page,
        get answer from server and passes form Applicant.
        For logged users.
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.edit_url)

        self.assertTrue(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_applicant.html')
        self.assertIsInstance(response.context['form'], ApplicantForm)

    def test_edit_page_contains_empty_form_with_empty_db(self):
        """
        Check for correct page with empty db
        """
        Applicant.objects.all().delete()
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.edit_url)
        empty_form = ApplicantForm()

        self.assertEqual(str(response.context['form']), str(empty_form))

    def test_edit_page_contains_form_with_applicant_data(self):
        """
        Check for correct data in the form
        """
        self.client.login(username='admin', password='admin')
        response = self.client.get(self.edit_url)
        applicant = Applicant.objects.first()

        self.assertContains(response, applicant.first_name, 1, 200)
        self.assertContains(response, applicant.last_name, 1, 200)
        self.assertIn(applicant.email, response.content)
        self.assertIn(str(applicant.birthday), response.content)


class JSONDataPageTest(TestCase):
    """
    Test for post data via AJAX
    """

    def test_edit_applicant_view_NOT_post_incorrect_data(self):
        """
        Test for post data via AJAX
        """
        ERROR_MESSAGE = 'This field is required.'
        url = reverse('hello:edit_applicant')
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}

        fields_list = ('first_name', 'last_name', 'email', 'jabber',
                       'skype', 'birthday')
        data = dict.fromkeys(fields_list, '')
        # data.update({'save_button': True})

        self.client.login(username='admin', password='admin')
        response = self.client.post(url, data, **kwargs)

        self.assertContains(response, ERROR_MESSAGE, 4, 200)

        applicant = Applicant.objects.first()
        for field in fields_list[:-1]:
            self.assertNotEqual(applicant.serializable_value(field),
                                data[field])

    def test_edit_applicant_view_POST_incorrect_data(self):
        """
        Test for post data via AJAX
        """
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('hello:edit_applicant')

        fields_list = ('first_name', 'last_name', 'email', 'jabber',
                       'skype', 'birthday')
        data_list = ('John', 'Galt', 'john.galt@gmail.com',
                     'john.galt@khavr.com', 'john.galt', '05/02/1879')
        data = dict(zip(fields_list, data_list))

        self.client.login(username='admin', password='admin')
        response = self.client.post(url, data, **kwargs)

        self.assertEqual(response.status_code, 200)

        new_applicant = Applicant.objects.first()

        for field in fields_list[:-1]:
            self.assertEqual(new_applicant.serializable_value(field),
                             data[field])
