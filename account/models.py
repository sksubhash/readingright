from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=254, verbose_name="Title")
    body = models.CharField(max_length=255, verbose_name="Body")

    def __str__(self):
        return self.name
