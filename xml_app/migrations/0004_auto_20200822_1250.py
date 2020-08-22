# Generated by Django 3.1 on 2020-08-22 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xml_app', '0003_filexml'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='mainFile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fileAttribute', to='xml_app.filexml'),
        ),
        migrations.AddField(
            model_name='element',
            name='mainFile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='xml_app.filexml'),
        ),
        migrations.AddField(
            model_name='parentship',
            name='mainFile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fileParentship', to='xml_app.filexml'),
        ),
    ]