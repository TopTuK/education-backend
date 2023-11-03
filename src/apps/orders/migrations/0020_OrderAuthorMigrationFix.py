# Generated by Django 3.2.9 on 2021-11-28 19:10

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0019_OrderAuthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='created_orders', to=settings.AUTH_USER_MODEL, verbose_name='Order author'),
        ),
    ]