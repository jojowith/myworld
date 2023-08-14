from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(default="", null=False)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            slugify(self.product_name, allow_unicode=True),
        }
        return redirect('profile:notownprofile', kwargs=kwargs)

# Create Profile When New User Signs Up
# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)
