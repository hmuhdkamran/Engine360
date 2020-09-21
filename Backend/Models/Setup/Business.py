from django.db import models


class Business(models.Model):
    BusinessId = models.UUIDField(primary_key=True, db_column='BusinessId')
    Abbreviation = models.TextField(null=False, db_column='Abbreviation')
    FullName = models.TextField(null=False, db_column='FullName')
    CreatedAt = models.DateTimeField(auto_now=True, db_column='CreatedAt')
    Address = models.TextField(default='', db_column='Address')

    class Meta:
        db_table = '"Setup"."Business"'