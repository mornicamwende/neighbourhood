from django.db import models
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from neighbourapp.models import Home


# Create your models here..
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default="welome to my hood", blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    home = models.ForeignKey(Home,on_delete=models.CASCADE, blank=True, null=True)

    def save_profile(self):
        self.save()
    
    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
