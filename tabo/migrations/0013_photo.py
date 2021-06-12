# Generated by Django 3.1.3 on 2021-06-12 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabo', '0012_posting_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('posting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tabo.posting')),
            ],
        ),
    ]
