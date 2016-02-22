
from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO
from django.db.models import get_models


class CouuntObjectsTest(TestCase):
    """
    Check the command to print models and counting number of objects
    """
    fixtures = ['initial_data.json']

    def test_output_and_count_objects_command(self):
        """
        Check the command to print models and counting number of objects
        """
        STDOUT = StringIO()
        STDERR = StringIO()

        call_command('count_objects', stdout=STDOUT)
        call_command('count_objects', stderr=STDERR)
        result_out = STDOUT.getvalue()
        result_err = STDERR.getvalue()
        list_models = get_models(include_auto_created=True)

        for model in list_models:
            self.assertIn(model._meta.object_name, result_out)
            self.assertIn('error: ' + model._meta.object_name, result_err)

        self.assertIn('Applicant: 1', result_out)
        self.assertIn('User: 1', result_out)
        self.assertIn('error: Applicant: 1', result_err)
        self.assertIn('error: User: 1', result_err)
