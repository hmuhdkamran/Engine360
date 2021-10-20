from django.db import models
import uuid

class Routes(models.Model):
    RouteId = models.UUIDField(null=False, primary_key=True)
    RouteName = models.TextField(null=False, unique=True)
    DisplayName = models.TextField(null=False, unique=True)
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = '"Role"."Routes"'
