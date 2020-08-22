# Generated by Django 3.1 on 2020-08-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml_app', '0002_auto_20200822_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileXML',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('hash', models.CharField(blank=True, max_length=255, null=True)),
                ('xmlFile', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]