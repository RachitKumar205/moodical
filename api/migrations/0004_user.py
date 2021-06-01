# Generated by Django 3.2 on 2021-05-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_songmood_mood'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mood', models.CharField(max_length=150)),
                ('followers', models.JSONField(blank=True, default='[]', null=True)),
            ],
        ),
    ]