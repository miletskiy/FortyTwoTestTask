
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import DatabaseRequest


class PriorityFieldTest(TestCase):
    """
    Tests for priority field
    """
    fixtures = ['initial_data.json']

    def test_for_saving_priority_instances_DatabaseRequest(self):
        """
        Test for saving priority DatabaseRequest models
        """
        self.client.ger(reverse('hello:contacts'))
        request_db = DatabaseRequest.objects.first()

        self.assertEqual(request_db.priority, 0)
        request_db.priority = 42
        request_db.save()

        request_db = DatabaseRequest.objects.first()

        self.assertEqual(request_db.priority, 42)
