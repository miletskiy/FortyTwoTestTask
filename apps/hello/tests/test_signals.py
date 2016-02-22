
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Applicant, DatabaseRequest, EventModel


class SignalsTest(TestCase):
    """
    Check signal processor for creating database entry
    """
    fixtures = ['initial_data.json']

    def test_saves_entry_for_creation_object(self):
        """
        Check signal processor saves info about creation object
        """
        self.assertEqual(EventModel.objects.all().count(), 0)
        self.client.get(reverse('hello:contacts'))
        event = EventModel.objects.last()

        self.assertEqual(DatabaseRequest.objects.all().count(), 1)
        self.assertEqual(EventModel.objects.all().count(), 1)
        self.assertEqual(event.event_type, 'ADDITION')

    def test_saves_entry_for_change_object(self):
        """
        Check signal processor saves info about change object
        """
        self.assertEqual(EventModel.objects.all().count(), 0)
        applicant = Applicant.objects.first()
        applicant.first_name = 'John'
        applicant.email = 'john.galt@gmail.com'
        applicant.save()

        self.assertEqual(EventModel.objects.all().count(), 1)
        event = EventModel.objects.last()

        self.assertEqual(event.sender, applicant._meta.model_name)
        self.assertEqual(event.event_type, 'CHANGE')

    def test_saves_entry_for_deletion_object(self):
        """
        Check signal processor saves info about deletion object
        """
        self.assertEqual(EventModel.objects.all().count(), 0)
        applicant = Applicant.objects.first()
        applicant.delete()

        self.assertEqual(EventModel.objects.all().count(), 1)
        self.assertEqual(event.sender, applicant._meta.model_name)
        self.assertEqual(event.event_type, 'DELETION')
