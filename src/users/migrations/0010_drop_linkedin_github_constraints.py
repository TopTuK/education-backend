# Generated by Django 3.2.16 on 2022-12-27 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_add_telegram_username'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique_github_username',
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='unique_linkedin_username',
        ),
    ]