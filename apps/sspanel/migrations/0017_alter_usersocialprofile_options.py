# Generated by Django 4.1.3 on 2022-11-19 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0016_alter_usersocialprofile_user_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usersocialprofile",
            options={"verbose_name": "用户社交资料", "verbose_name_plural": "用户社交资料"},
        ),
    ]
