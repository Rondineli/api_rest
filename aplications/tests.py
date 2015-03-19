#!/usr/bin/python
# -*- coding: utf-8; -*-

from django.test import Client, TestCase
from django.contrib.auth.models import User


class ServerTests(TestCase):

    def login_api(self):
        try:
            temp_user = User.objects.create_user(
                username='rondineli',
                password='rondigomes',
                email='r@r.com'
            )
        except:
            pass

        self.client = Client()
        response = self.client.post(
            '/api-auth/login/', {
                'username': u'rondineli',
                'password': u'rondigomes'
            }
        )

    def setUp(self):
        self.assertEqual(1 + 1, 2)

    @login_api
    def test_list_aplications(self):
        response = self.client.get(
            '/aplications/', {
                'format': 'json'
            }
        )
        self.assertEqual(response.status_code, 200)

    @login_api
    def test_create_aplications(self):
        response = self.client.post(
            '/aplications/', {
                'aplication': 'apache',
                'server': 1
            }
        )
        self.assertEqual(response.status_code, 201)

    @login_api
    def test_delete_aplications(self):
        response = self.client.delete(
            '/aplications/1', {
                'format': 'json'
            }
        )
        self.assertEqual(response.status_code, 204)
