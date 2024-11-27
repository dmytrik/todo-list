from django.contrib.auth.models import AbstractUser
from django.db import models

from task.models import Task


class User(AbstractUser):
    tasks = models.ManyToManyField(Task, related_name="users")
