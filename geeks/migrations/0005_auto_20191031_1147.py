# Generated by Django 2.2.6 on 2019-10-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0004_auto_20191031_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='geeks_field',
            field=models.CharField(error_messages={'null': 'The Field you enetered is null.'}, max_length=200),
        ),
    ]
