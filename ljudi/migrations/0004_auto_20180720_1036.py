# Generated by Django 2.0.7 on 2018-07-20 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ljudi', '0003_auto_20180719_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template_resenja',
            name='path',
        ),
        migrations.AddField(
            model_name='template_resenja',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='resenja/'),
        ),
        migrations.AddField(
            model_name='template_resenja',
            name='opis',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='template_resenja',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 20, 8, 36, 45, 349344, tzinfo=utc)),
            preserve_default=False,
        ),
    ]