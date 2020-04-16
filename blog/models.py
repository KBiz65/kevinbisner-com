from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    published_on = models.DateTimeField(null=True, default=None)  # set default
    created_on = models.DateTimeField(auto_now_add=True)  # adds the current
    # DateTime when the object is created, and never changes it
    updated_on = models.DateTimeField(auto_now=True)  # adds the current
    # DateTime whenever the object is saved.

    def __str__(self):
        return f"{self.title}"
