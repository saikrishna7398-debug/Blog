from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.ImageField(default="users/profile/i.jpeg", upload_to="users/profile")

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
