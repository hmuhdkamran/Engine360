from django.db import models
import uuid

from .Role.user import User
from .Role.users import Users
from .Role.routes import Routes
from .Role.roles import Roles
from .Role.roles_routes import RolesRoutesMap
from .Role.user_roles import UsersRolesMap
from .Role.user_session import UserSession
from .Role.queries import Queries
from .Setup.Business import Business


class LogEntryForException(models.Model):
    Exception = models.TextField(null=False)
    RequestUrl = models.TextField(default='')
    UserAgent = models.TextField(default='')
    IpAddress = models.TextField(default='')
    CreatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"LogEntryForException"'
