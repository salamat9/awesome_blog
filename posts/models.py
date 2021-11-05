from django.db import models
from django.contrib.auth.models import User
# new
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    description = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    # new
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')

    # new
    class Meta:
        # новые посты будут в начале
        ordering = ['-created']

    def __str__(self):
        return self.title

