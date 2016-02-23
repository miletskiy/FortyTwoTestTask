
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import EventModel


@receiver((post_save, post_delete))
def save_to_db_changes_of_objects_signal(sender, **kwargs):
    """
    Signal for creation instance of the EventModel about
    changes of objects
    """
    created = kwargs.get('created')
    name_sender = sender._meta.object_name

    if created is None:
        event_type = 'DELETION'

    elif created:
        event_type = 'ADDITION'

    else:
        event_type = 'CHANGE'

    if name_sender != 'EventModel':
        EventModel.objects.create(sender=name_sender,
                                  event_type=event_type)
