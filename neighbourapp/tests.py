from django.test import TestCase
from .models import post
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class TestPost(TestCase):
    def setUp(self):
        self.user = User(username='Mornica')
        self.user.save()
        self.post_test = post(id=1,caption='Denim wear', image='default.jpg', title='fashion')

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, post))

    def test_save_post(self):
        posts = post.objects.all()

    def test_delete_post(self):
        before = Profile.objects.all()
        after = Profile.objects.all()
        self.assertTrue(len(before) == len(after))


