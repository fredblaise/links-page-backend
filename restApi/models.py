from django.db import models


# Create your models here.
class LinkPage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=300)

    DisplayFields = ["id", "title", "subtitle", "profile_image"]

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    icon = models.CharField(max_length=300)
    color = models.CharField(max_length=100)

    DisplayFields = ["id", "title", "link", "icon", "color"]

    def __str__(self):
        return self.title
