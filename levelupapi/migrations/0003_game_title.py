# Generated by Django 4.2.4 on 2023-08-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_rename_type_gametype_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='title',
            field=models.CharField(default='Default Title', max_length=250),
        ),
    ]