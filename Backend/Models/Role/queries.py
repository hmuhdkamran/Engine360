#
#   Auther: H.Muhammad Kamran
#   email: hmuhdkamran@gmail.com
#   contact: +92 (313 / 333) 9112 845
#

from django.db import models
import uuid

class Queries(models.Model):
    QueryId = models.UUIDField(null=False, primary_key=True, db_column='QueryId')
    FullName = models.TextField(null=False, unique=True, db_column='FullName')
    Description = models.TextField(null=False, db_column='Description')
    Status = models.IntegerField(null=False, db_column='Status')

    class Meta:
        db_table = '"Role"."Queries"'
