# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20181201_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('WAIT_BUYER_PAY', '交易创建'), ('PAYING', '待支付'), ('TRADE_CLOSE', '交易关闭'), ('TRADE_SUCCESS', '成功'), ('TRADE_FINISHED', '交易结束')], default='PAYING', max_length=20, verbose_name='交易状态'),
        ),
    ]
