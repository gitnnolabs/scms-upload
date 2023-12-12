# Generated by Django 4.2.6 on 2023-12-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "acron",
                    models.TextField(
                        blank=True, null=True, verbose_name="Collection Acronym"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        blank=True, null=True, verbose_name="Collection Name"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        blank=True, null=True, verbose_name="Language Name"
                    ),
                ),
                (
                    "code2",
                    models.TextField(
                        blank=True, null=True, verbose_name="Language code 2"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
            },
        ),
        migrations.CreateModel(
            name="WebSiteConfiguration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Website URL",
                    ),
                ),
                (
                    "api_url_article",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Article API URL",
                    ),
                ),
                (
                    "api_url_issue",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Issue API URL",
                    ),
                ),
                (
                    "api_url_journal",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Journal API URL",
                    ),
                ),
                (
                    "api_get_token_url",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Get token API URL",
                    ),
                ),
                (
                    "api_username",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                (
                    "api_password",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
                ("api_token", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "db_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Database name",
                    ),
                ),
                (
                    "db_uri",
                    models.CharField(
                        blank=True,
                        help_text="mongodb://login:password@host:port/database",
                        max_length=255,
                        null=True,
                        verbose_name="Mongodb Info",
                    ),
                ),
                (
                    "purpose",
                    models.CharField(
                        blank=True,
                        choices=[("QA", "QA"), ("PUBLIC", "PUBLIC")],
                        max_length=25,
                        null=True,
                        verbose_name="Purpose",
                    ),
                ),
                ("enabled", models.BooleanField()),
                (
                    "collection",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="collection.collection",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["purpose"], name="collection__purpose_fd1c7c_idx"
                    ),
                    models.Index(fields=["url"], name="collection__url_a79c69_idx"),
                ],
            },
        ),
    ]
