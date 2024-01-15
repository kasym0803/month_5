from django.contrib.auth.models import User
from django.db import models


class Confirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()
