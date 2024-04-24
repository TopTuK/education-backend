# Generated by Django 3.2.12 on 2022-04-04 20:22

from django.db import migrations, models


def set_ue_rate_for_stripe_bank(apps, schema_editor):
    del schema_editor

    apps.get_model("orders.Order").objects.filter(
        desired_bank="stripe",
    ).update(
        ue_rate=100,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0021_OrderConstraintForProductItemsCountCheck"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="ue_rate",
            field=models.IntegerField(default=1, verbose_name="Purchase-time UE rate"),
            preserve_default=False,
        ),
        migrations.RunPython(set_ue_rate_for_stripe_bank),
    ]
