# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import yandex_kassa.utils


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_kassa', '0006_auto_20170525_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_number',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_number',
            field=models.CharField(default=yandex_kassa.utils.get_uuid, unique=True, max_length=64, verbose_name=b'ID \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
        ),
    ]
