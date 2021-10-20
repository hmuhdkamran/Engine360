from django.db import models
import uuid

from .roles import Roles
from .routes import Routes

class RolesRoutesMap(models.Model):
    RoleRouteMapId = models.UUIDField(primary_key=True, null=False)
    RoleId = models.ForeignKey(Roles, db_column='RoleId', on_delete=models.CASCADE)
    RouteId = models.ForeignKey(Routes, db_column='RouteId', on_delete=models.CASCADE)
    Operation = models.TextField(db_column='Operation')
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = '"Role"."RolesRoutesMap"'
        constraints = [
            models.UniqueConstraint(fields=['RoleId', 'RouteId'], name='Uk_RolesRoutesMap_RoleId_RouteId')
        ]
