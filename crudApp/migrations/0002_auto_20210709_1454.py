# Generated by Django 3.1.7 on 2021-07-09 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='saddress',
            new_name='sDateofbirth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sno',
            new_name='sRollNo',
        ),
    ]
