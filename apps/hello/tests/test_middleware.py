
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import DatabaseRequest


class DatabaseRequestTest(TestCase):
    """
    Test for middleware
    """

    def test_middleware_saves_normal_requests_to_the_database(self):
        """
        Check that middleware saves requests to the database
        """
        quantity_reqs = DatabaseRequest.objects.all().count()
        self.assertEqual(quantity_reqs, 0)

        self.client.get(reverse('hello:contacts'))
        quantity_reqs = DatabaseRequest.objects.all()

        self.assertEqual(quantity_reqs, 1)

        last_reqeust = DatabaseRequest.objects.last()
        self.assertEqual(last_reqeust.path, reverse('hello:contacts'))

    def test_middleware_does_not_save_ajax_requests_to_the_database(self):
        """
        Check that middleware does not save ajax requests to the database
        """
        quantity_reqs = DatabaseRequest.objects.all().count()
        self.assertEqual(quantity_reqs, 0)

        self.client.get(reverse('hello:requests'),
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        quantity_reqs = DatabaseRequest.objects.all().count()
        self.assertEqual(quantity_reqs, 0)
