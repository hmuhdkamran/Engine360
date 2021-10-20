#
#   Auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from django.db import models
import uuid

class Roles(models.Model):
    RoleId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    ParentRoleId = models.UUIDField(null=True)
    FullName = models.TextField(null=False, unique=True)
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = '"Role"."Roles"'
