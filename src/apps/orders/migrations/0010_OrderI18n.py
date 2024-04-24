# Generated by Django 3.1.4 on 2020-12-27 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.orders.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0014_CourseWelcomeLetter"),
        ("orders", "0009_Gifts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="bundle",
            field=apps.orders.fields.ItemField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="products.bundle", verbose_name="Bundle"),
        ),
        migrations.AlterField(
            model_name="order",
            name="course",
            field=apps.orders.fields.ItemField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="products.course", verbose_name="Course"),
        ),
        migrations.AlterField(
            model_name="order",
            name="gift_message",
            field=models.TextField(default="", verbose_name="Gift message", blank=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="giver",
            field=models.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_gifts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Giver",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Price"),
        ),
        migrations.AlterField(
            model_name="order",
            name="record",
            field=apps.orders.fields.ItemField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="products.record", verbose_name="Record"),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name="User"),
        ),
    ]
