from django.db import models
import uuid

from .users import Users
from .roles_routes import RolesRoutesMap


class UsersRolesMap(models.Model):
    UserRoleMapId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    UserId = models.UUIDField(null=False,db_column='UserId')
    RoleRouteMapId = models.UUIDField(null=False,db_column='RoleRouteMapId')
    Status = models.BooleanField(null=False)

    class Meta:
        db_table = '"Role"."UsersRolesMap"'
        constraints = [
            models.UniqueConstraint(fields=['UserId', 'RoleRouteMapId'], name='Uk_UsersRolesMap_UserId_RoleRouteMapId')
        ]

class VwUsersRolesMap(models.Model):
    UserRoleMapId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    Status = models.BooleanField(null=False)
    DisplayName = models.TextField(null=True, db_column='DisplayName')
    UserId = models.UUIDField(null=False,db_column='UserId')
    RoleRouteMapId = models.UUIDField(null=False,db_column='RoleRouteMapId')
    Operation = models.TextField(null=True, db_column='Operation')
    Role = models.TextField(null=True, db_column='Role')
    RouteName = models.TextField(null=True, db_column='RouteName')
    RoleId = models.UUIDField(null=False,db_column='RoleId')
    RouteId = models.UUIDField(null=False,db_column='RouteId')


    class Meta:
        db_table = '"Role"."VwUsersRolesMap"'        
