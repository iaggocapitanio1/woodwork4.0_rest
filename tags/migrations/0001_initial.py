# Generated by Django 3.2.18 on 2023-06-06 14:08

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import hashid_field.field
import utilities.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=16, prefix='tags_', primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to=utilities.functions.upload_pdf_to)),
                ('excel', models.FileField(upload_to=utilities.functions.upload_pdf_to)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TagResult',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=16, prefix='tag_result_', primary_key=True, serialize=False)),
                ('pdf', models.FileField(upload_to=utilities.functions.upload_result_pdf_to)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
