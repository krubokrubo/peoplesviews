# Generated by Django 2.2.6 on 2019-10-14 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20191014_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='voted',
            new_name='submitted',
        ),
    ]