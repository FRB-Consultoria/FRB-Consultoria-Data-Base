from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    user_level = models.CharField(max_length=20)
    power_bi_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    client = models.ForeignKey(
        "clients.Client",
        related_name="users",
        on_delete=models.CASCADE
    )
    
    def __repr__(self) -> str:
        return f"<User ({self.id}) - {self.username}>"