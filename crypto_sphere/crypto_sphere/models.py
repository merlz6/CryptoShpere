from django.db import models


class User(models.Model):
    username = models.charField(max_length=255)
    password = models.Password(max_length=255)
