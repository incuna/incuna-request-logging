from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from logger.middleware import LogRequestMiddleware


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
