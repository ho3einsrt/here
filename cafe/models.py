from django.db import models


class Cafes(models.Model):
    name = models.CharField(max_length=40)
    instagram = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name
