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

    @login_api
    def test_list_servers(self):
        response = self.client.get(
            '/servers/', {
                'format': 'json'
            }
        )
        self.assertEqual(response.status_code, 200)

    @login_api
    def test_create_servers(self):
        response = self.client.post(
            '/servers/', {
                'server_name': 'host_test',
                'is_active': True,
                'ip': 'qqcoisa'
            }
        )
        self.assertEqual(response.status_code, 201)

    @login_api
    def test_delete_server(self):
        response = self.client.delete(
            '/servers/1', {
                'format': 'json'
            }
        )
        self.assertEqual(response.status_code, 204)
