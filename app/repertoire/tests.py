import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from .models import File, Work
from .serializers import FileSerializer, WorkSerializer


# Create your tests here.
class StoringFileTestCase(APITestCase):
    def test_storing_file_name(self):
        data = {"filename": "sony.csv"}
        response = self.client.post('/files/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

