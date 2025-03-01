# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.0.2 on 2022-04-20 11:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0017_alter_verifiedemail_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="language",
            field=models.CharField(
                choices=settings.LANGUAGES,
                max_length=10,
                verbose_name="Interface Language",
            ),
        ),
    ]
