# Generated by Django 3.2 on 2021-05-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]