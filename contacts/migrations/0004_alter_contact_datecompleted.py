# Generated by Django 5.1 on 2024-09-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_rename_description_contact_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
