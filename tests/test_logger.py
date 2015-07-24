from django.test import TestCase
from incuna_test_utils.utils import field_names

from logger.models import Log


class TestLog(TestCase):
    def test_fields(self):
        expected_fields = {
            'id',
            'user_pk',
            'registration_date',
            'timestamp',
            'url',
            'request_method',
        }

        self.assertEqual(field_names(Log), expected_fields)
