from django.db import models

from cafe.models import Cafes


class Tables(models.Model):
    token = models.CharField(max_length=30)
    cafe = models.ForeignKey(Cafes, null=True, on_delete=models.SET_NULL)