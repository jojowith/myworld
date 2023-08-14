from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class PostInfo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    brief = models.CharField(max_length=50)
    body = models.TextField()
    linkage = models.URLField(max_length=140, blank=True)
    Cover = models.ImageField(upload_to='media/postCoverPicture/', blank=True)
    image = models.ImageField(upload_to='media/postPicture/', blank=True)
    video = models.FileField(upload_to='media/postVideo/', blank=True)
    likes= models.ManyToManyField(User, related_name="post_like", blank=True)
    dislike= models.ManyToManyField(User, related_name="post_dislike", blank=True)
    def number_of_like(self):
        return self.likes.count()
    def number_of_dislike(self):
        return self.dislike.count()

    def __str__(self):
        return (
            f"{self.title}"
            f"{self.creator}"
            f"{self.brief}..."
            f"{self.Cover}"
        )
