# Generated by Django 4.1.9 on 2023-06-22 08:21

import uuid

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("homework", "0011_AnswerImage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reaction",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("slug", models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ("emoji", models.CharField(max_length=10)),
                ("answer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reactions", to="homework.answer")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reactions", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Reaction",
                "verbose_name_plural": "Reactions",
                "ordering": ["created"],
            },
        ),
        migrations.AddConstraint(
            model_name="reaction",
            constraint=models.UniqueConstraint(fields=("author", "answer", "emoji"), name="Unique emoji per author"),
        ),
    ]