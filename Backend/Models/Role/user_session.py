from django.db import models
import uuid

from .users import Users


class UserSession(models.Model):
    SessionId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, db_column='UserId')
    Expiry = models.DateTimeField()
    IsValid = models.BooleanField(default=True)
    ChallengeCheck = models.TextField(default='')
    CreatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"Role"."UserSessionMap"'
