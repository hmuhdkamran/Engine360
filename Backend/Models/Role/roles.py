from django.db import models
import uuid


class Roles(models.Model):
    RoleId = models.UUIDField(null=False, primary_key=True)
    ParentRoleId = models.UUIDField(null=False)
    FullName = models.TextField(null=False, unique=True)
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = '"Role"."Roles"'
