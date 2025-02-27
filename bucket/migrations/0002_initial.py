# Generated by Django 3.2.18 on 2023-06-06 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bucket', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to=settings.AUTH_USER_MODEL, verbose_name='Resource Owner'),
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='bucket.folder'),
        ),
        migrations.AddConstraint(
            model_name='folder',
            constraint=models.UniqueConstraint(fields=('name', 'parent', 'user', 'budget'), name='unique_Folder'),
        ),
        migrations.AddConstraint(
            model_name='file',
            constraint=models.UniqueConstraint(fields=('file', 'folder'), name='unique_File'),
        ),
    ]
