from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self) -> str:
        return self.content