# Generated by Django 3.1 on 2020-08-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='attribute',
            new_name='key',
        ),
        migrations.AddField(
            model_name='attribute',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
