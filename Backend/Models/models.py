from django.db import models


class Roles(models.Model):
    RoleId = models.UUIDField(null=False, primary_key=True)
    ParentRoleId = models.UUIDField(null=False)
    FullName = models.TextField(null=False, unique=True)
    Status = models.BooleanField(default=False)


class Routes(models.Model):
    RouteId = models.UUIDField(null=False, primary_key=True)
    RouteName = models.TextField(null=False, unique=True)
    DisplayName = models.TextField(null=False, unique=True)
    Status = models.BooleanField(default=False)


class RolesRoutesMap(models.Model):
    RoleRouteMapId = models.UUIDField(null=False, primary_key=True)
    RoleId = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='Fk_RolesRoutesMap_RoleId')
    RouteId = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name='Fk_RolesRoutesMap_RouteId')
    Status = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['RoleId', 'RouteId'], name='Uk_RolesRoutesMap_RoleId_RouteId')
        ]


class User(models.Model):
    UserId = models.UUIDField(null=False, primary_key=True)
    Username = models.TextField(null=False, unique=True)
    DisplayName = models.TextField(null=False)
    Language = models.TextField(null=False)
    Password = models.TextField(null=False)
    Salt = models.TextField(null=False)
    Status = models.BooleanField(null=False)


class UsersRolesMap(models.Model):
    UserRoleMapId = models.UUIDField(null=False, primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_UserId')
    RoleRouteMapId = models.ForeignKey(RolesRoutesMap, on_delete=models.CASCADE, related_name='Fk_UsersRolesMap_RoleRouteMapId')
    Status = models.BooleanField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['UserId', 'RoleRouteMapId'], name='Uk_UsersRolesMap_UserId_RoleRouteMapId')
        ]