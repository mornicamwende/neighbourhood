from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Mornica')
        self.user.save()

        self.profile_test = Profile(user=self.user, image='default.jpg' )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    
    