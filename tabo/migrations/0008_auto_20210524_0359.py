# Generated by Django 3.1.3 on 2021-05-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabo', '0007_auto_20210524_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='tag',
            field=models.CharField(choices=[('C', 'C Language'), ('Jave', 'Java Language')], max_length=10),
        ),
    ]
