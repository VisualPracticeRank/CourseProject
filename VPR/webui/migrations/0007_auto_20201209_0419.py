# Generated by Django 3.1.3 on 2020-12-09 04:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0006_auto_20201209_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='id',
            field=models.UUIDField(default=uuid.UUID('134737d8-2920-42de-a859-bf48f6a98c6e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
