# Generated by Django 3.1.3 on 2020-12-13 04:54

from django.db import migrations, models
import webui.models


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0012_auto_20201213_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='qrels',
            field=models.FileField(default='', upload_to=webui.models.qrels_id_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='queries',
            field=models.FileField(default='', upload_to=webui.models.queries_id_path),
            preserve_default=False,
        ),
    ]