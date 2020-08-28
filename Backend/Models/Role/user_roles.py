from django.db import models
import uuid

from .user import User
from .roles_routes import RolesRoutesMap

class UsersRolesMap(models.Model):
    UserRoleMapId = models.UUIDField(null=False, primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_UserId')
    RoleRouteMapId = models.ForeignKey(RolesRoutesMap, on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_RoleRouteMapId')
    Status = models.BooleanField(null=False)

    class Meta:
        db_table = '"Role"."UsersRolesMap"'
        constraints = [
            models.UniqueConstraint(fields=['UserId', 'RoleRouteMapId'], name='Uk_UsersRolesMap_UserId_RoleRouteMapId')
        ]