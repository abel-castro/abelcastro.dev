from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    meta_description = models.TextField(max_length=155)
    content = MartorField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published and not self.date:
            self.date = timezone.now().date()
        return super().save(*args, **kwargs)
