# Generated by Django 2.2.6 on 2019-11-05 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geeksmodel',
            old_name='geeks_mail',
            new_name='title',
        ),
    ]
