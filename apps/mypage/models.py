from django.db import models

from apps.account.models import User
from core.models import BaseModel


class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    due = models.DateTimeField()

    class Meta:
        db_table = "todo"
