import datetime

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
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

    def test_log_request(self):
        factory = RequestFactory()
        request = factory.get('/admin')
        request.user = User.objects.create()

        log = Log.objects.from_request(request)

        self.assertEqual(log.user_pk, request.user.pk)
        self.assertEqual(log.registration_date, request.user.date_joined)
        self.assertIsInstance(log.timestamp, datetime.datetime)
        self.assertEqual(log.url, request.build_absolute_uri())
        self.assertEqual(log.request_method, request.method)
