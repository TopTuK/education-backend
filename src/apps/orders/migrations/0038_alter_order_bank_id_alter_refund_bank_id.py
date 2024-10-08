# Generated by Django 4.2.13 on 2024-08-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0037_DropUnpaid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="bank_id",
            field=models.CharField(
                blank=True,
                choices=[
                    ("dolyame", "Dolyame"),
                    ("stripe", "Stripe USD"),
                    ("stripe_kz", "Stripe KZT"),
                    ("tinkoff_bank", "Tinkoff"),
                    ("zero_price", "Zero Price"),
                ],
                max_length=32,
                verbose_name="User-requested bank string",
            ),
        ),
        migrations.AlterField(
            model_name="refund",
            name="bank_id",
            field=models.CharField(
                blank=True,
                choices=[
                    ("dolyame", "Dolyame"),
                    ("stripe", "Stripe USD"),
                    ("stripe_kz", "Stripe KZT"),
                    ("tinkoff_bank", "Tinkoff"),
                    ("zero_price", "Zero Price"),
                ],
                max_length=32,
                verbose_name="Order bank at the moment of refund",
            ),
        ),
    ]
