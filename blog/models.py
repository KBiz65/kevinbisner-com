from django.db import models


class Blogpost(models.Model):
    blog_user = models.CharField(max_length=20)
    blog_title = models.CharField(max_length=120, default="Temporary Title")
    blog_text = models.TextField(blank=False, null=False)
    blog_date = models.DateField()
