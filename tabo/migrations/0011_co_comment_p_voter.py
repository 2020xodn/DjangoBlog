# Generated by Django 3.1.3 on 2021-05-24 20:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tabo', '0010_auto_20210525_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='co_comment_p',
            name='voter',
            field=models.ManyToManyField(related_name='voter_co_comment_p', to=settings.AUTH_USER_MODEL),
        ),
    ]