from django.db import models
import uuid

from .user import User


class UserSession(models.Model):
    SessionId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Expiry = models.DateTimeField()
    IsValid = models.BooleanField(default=True)
    ChallengeCheck = models.TextField(default='')
    CreatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"Role"."UserSessionMap"'
