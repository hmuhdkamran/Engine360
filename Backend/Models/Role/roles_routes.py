from django.db import models
import uuid

from .roles import Roles
from .routes import Routes


class RolesRoutesMap(models.Model):
    RoleRouteMapId = models.UUIDField(null=False, primary_key=True)
    RoleId = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='Fk_RolesRoutesMap_RoleId',
                               db_column='RoleId')
    RouteId = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name='Fk_RolesRoutesMap_RouteId',
                                db_column='RouteId')
    Operation = models.TextField(db_column='Operation')
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = '"Role"."RolesRoutesMap"'
        constraints = [
            models.UniqueConstraint(fields=['RoleId', 'RouteId'], name='Uk_RolesRoutesMap_RoleId_RouteId')
        ]
