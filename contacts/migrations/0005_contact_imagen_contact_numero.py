# Generated by Django 5.1 on 2024-09-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_datecompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='imagen',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='numero',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
