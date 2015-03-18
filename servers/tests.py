#!/usr/bin/python
# -*- coding: utf-8; -*-

from django.test import Client
from django.test import TestCase


class ServerTests(TestCase):

    def test_create_server(self):
        c = Client()
        response = c.get('/users/?format=json')
        self.assertEqual(response.status_code, 200)
