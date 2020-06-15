from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    address = models.CharField(max_length=50)
    bio = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="profile_img")

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
            super(Profile, self).save(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)



# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User)

    


