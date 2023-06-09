from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Core(models.Model):
    title = models.CharField(max_lenth=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=100, unique=True)
    update = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('core:single', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
