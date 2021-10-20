from django.db import models
import uuid
from .Users import Users
from .RolesRoutesMap import RolesRoutesMap


class UsersRolesMap(models.Model):
    UserRoleMapId = models.UUIDField(null=True, db_column='UserRoleMapId', primary_key=True)
    UserId = models.ForeignKey(Users, null=True, db_column='UserId', on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_UserId')
    RoleRouteMapId = models.ForeignKey(RolesRoutesMap, null=True, db_column='RoleRouteMapId', on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_RoleRouteMapId')
    Status = models.BooleanField(null=True, db_column='Status')
    
    class Meta:
        db_table = '"Role"."UsersRolesMap"'