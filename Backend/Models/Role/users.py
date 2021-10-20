from django.db import models
import uuid

class Users(models.Model):
    UserId = models.UUIDField(null=False, db_column='UserId', primary_key=True)
    Username = models.TextField(null=True, db_column='Username')
    DisplayName = models.TextField(null=True, db_column='DisplayName')
    Language = models.TextField(null=True, db_column='Language')
    Password = models.TextField(null=True, db_column='Password')
    Salt = models.TextField(null=True, db_column='Salt')
    Status = models.BooleanField(null=True, db_column='Status')
    
    class Meta:
        db_table = '"Role"."Users"'

class UserSeller(models.Model):
    UserSellerId = models.UUIDField(null=False, db_column='UserSellerId', primary_key=True)
    UserId = models.UUIDField(null=False, db_column='UserId')
    SellerId = models.UUIDField(null=False, db_column='SellerId')
    
    class Meta:
        db_table = '"Role"."UserSellerLink"'        