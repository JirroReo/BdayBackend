from django.db import models

# Create your models here.

class Message(models.Model):
    message = models.TextField()
    sender = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender