import datetime
from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from incuna_test_utils.utils import field_names

from logger.middleware import LogRequestMiddleware
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


class TestLogRequestMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = LogRequestMiddleware()

    def test_authenticated(self):
        request = self.factory.get('/admin')
        request.user = User.objects.create()

        with patch('logger.models.LogManager.from_request') as from_request:
            response = self.middleware.process_request(request)

        from_request.assert_called_once_with(request)
        self.assertIsNone(response)

    def test_anonymous(self):
        request = self.factory.get('/admin')
        request.user = AnonymousUser()

        with patch('logger.models.LogManager.from_request') as from_request:
            response = self.middleware.process_request(request)

        self.assertFalse(from_request.called)
        self.assertIsNone(response)
