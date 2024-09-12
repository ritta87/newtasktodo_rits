
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo_db(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title