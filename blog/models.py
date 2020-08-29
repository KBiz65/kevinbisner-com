from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    # published_on = models.DateTimeField(null=True, default=None)  # set default
    created_on = models.DateTimeField(auto_now_add=False)  # adds the current
    # DateTime when the object is created, and never changes it
    # updated_on = models.DateTimeField(auto_now=True)  # adds the current
    # DateTime whenever the object is saved.

    def __str__(self):
        return f"{self.title}"

    # @property
    # def has_been_updated(self):
    #     return self.published_on < self.updated_on

    # def save(self, *args, **kwargs):
    #     """
    #     Customize Model.save() behavior to check if the published boolean has been
    #     set to True, if so, then set the published_on value to either timezone.now()
    #     or datetime.datetime.now() depending on whether settings.USE_TZ is true.
    #     https://docs.djangoproject.com/en/3.0/topics/db/models/#overriding-model-methods
    #     """

    #     if self.published and self.published_on is None:

    #         if settings.USE_TZ:
    #             self.published_on = timezone.now()
    #         else:
    #             import datetime as dt
    #             self.published_on = dt.datetime.utcnow()

    #     super().save(*args, **kwargs)
