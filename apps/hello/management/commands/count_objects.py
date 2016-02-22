
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    """
    Check the command to print models and counting number of objects
    """

    def handle_noargs(self, **options):
        pass