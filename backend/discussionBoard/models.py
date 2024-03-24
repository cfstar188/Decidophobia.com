from django.db import models
from users.models import CustomUser as User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=150)
    replyTo = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.message