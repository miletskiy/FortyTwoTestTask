
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
        self.client.get(reverse('hello:contacts'))
        request_db = DatabaseRequest.objects.first()

        self.assertEqual(request_db.priority, 0)
        request_db.priority = 42
        request_db.save()

        request_db = DatabaseRequest.objects.first()

        self.assertEqual(request_db.priority, 42)

    def test_sorting_by_priority(self):
        """
        Test for sorting by priority field DatabaseRequest model
        """
        # The sorting link is presents on the page
        order_by = '?order_by=priority'
        self.client.get(reverse('hello:contacts'))
        response = self.client.get(reverse('hello:requests'))
        self.assertIn(order_by, response.content)

        # After click on the order_by link webrequests sorting by priority
        for i in range(5):
            self.client.get(reverse('hello:contacts'))

        for i in range(1, 6):
            webrequest = DatabaseRequest.objects.get(pk=i)
            webrequest.priority = i
            webrequest.save()

        webrequests = DatabaseRequest.objects.all()
        response = self.client.get(reverse('hello:requests')+order_by)
        webrequests = webrequests.order_by('priority')

        for i in range(5):
            self.assertEqual(response.context['requests'][i], webrequests[i])

        # After another click on the order_by link webrequest reversing
        response = self.client.get(reverse('hello:requests') +
                                   order_by+'&reverse=true')
        webrequests = webrequests.reverse()

        for i in range(5):
            self.assertEqual(response.context['requests'][i], webrequests[i])
