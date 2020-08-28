from django.db import models
import uuid

class User(models.Model):
    UserId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    Username = models.TextField(null=False, unique=True)
    DisplayName = models.TextField(null=False)
    Language = models.TextField(null=False)
    Password = models.TextField(null=False)
    Salt = models.TextField(null=False)
    Status = models.BooleanField(null=False)

    class Meta:
        db_table = '"Role"."Users"'