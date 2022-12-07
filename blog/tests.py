from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
# Create your tests here.

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='category test')
        test_user1 = User.objects.create_user(username='test_user', password='123456789asd')
        test_post = Post.objects.create(category_id=1, title='post test', content='test OK', slug='hadi_bebek', author_id=1, status='published' )
        
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user')
        self.assertEqual(title, 'post test')
        self.assertEqual(content, 'test OK')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'post test')
        self.assertEqual(str(cat), 'category test')