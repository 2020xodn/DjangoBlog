# Generated by Django 3.1.3 on 2021-05-23 16:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tabo', '0005_comment_comment_p'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_comment_p',
            new_name='Co_Comment_P',
        ),
    ]
