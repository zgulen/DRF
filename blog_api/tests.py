from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

# Create your tests here.

class PostTest(APITestCase):
    def test_view_post(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def create_post(self):
        self.test_category = Category.objects.create(name='APItest')
        self.test.post = User.objects.create_user(username='ApıTestUser', password=123456789)
        data = {
            'title':'test',
            'author':'1',
            'content': 'TEST'
        }
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        