# Generated by Django 3.1 on 2020-09-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='ParentRoleId',
            field=models.UUIDField(null=True),
        ),
    ]
