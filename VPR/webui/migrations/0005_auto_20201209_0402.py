# Generated by Django 3.1.3 on 2020-12-09 04:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0004_auto_20201209_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='id',
            field=models.UUIDField(default=uuid.UUID('28dd3eed-594d-4d3f-9d56-0cefc783ac4a'), editable=False, primary_key=True, serialize=False),
        ),
    ]