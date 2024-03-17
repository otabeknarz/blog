from django.db import models
import uuid
from django.contrib.auth.models import User


class Post(models.Model):
    class Publish(models.TextChoices):
        PUBLISHED = ('PB', 'Published')
        DRAFT = ('DR', 'Draft')

    UUID = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    images = models.ManyToManyField('Image', blank=True, related_name='posts')
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    text = models.TextField()
    status = models.CharField(max_length=2, choices=Publish.choices, default=Publish.PUBLISHED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created']


class Image(models.Model):
    UUID = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='post_images/')
