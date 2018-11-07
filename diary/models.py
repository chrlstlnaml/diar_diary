from django.db import models
from django.utils import timezone

class Diary(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_visible = models.BooleanField(default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Plan(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    is_done = models.BooleanField(default=False)


    def publish(self):
        self.save()

    def __str__(self):
        return self.text