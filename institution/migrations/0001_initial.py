# Generated by Django 4.2.6 on 2023-12-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("location", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Institution",
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
                ("name", models.TextField(blank=True, null=True, verbose_name="Nome")),
                (
                    "institution_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", ""),
                            ("FUNDER", "agência de apoio à pesquisa"),
                            (
                                "SCHOLARLY",
                                "universidade e instâncias ligadas à universidades",
                            ),
                            ("GOVERNMENT", "empresa ou instituto ligadas ao governo"),
                            ("PRIVATE", "organização privada"),
                            ("NON_PROFIT", "organização sem fins de lucros"),
                            (
                                "SOCIETY",
                                "sociedade científica, associação pós-graduação, associação profissional",
                            ),
                            ("OTHER", "outros"),
                        ],
                        max_length=255,
                        null=True,
                        verbose_name="Institution Type",
                    ),
                ),
                (
                    "acronym",
                    models.TextField(
                        blank=True, null=True, verbose_name="Institution Acronym"
                    ),
                ),
                (
                    "level_1",
                    models.TextField(
                        blank=True, null=True, verbose_name="Organization Level 1"
                    ),
                ),
                (
                    "level_2",
                    models.TextField(
                        blank=True, null=True, verbose_name="Organization Level 2"
                    ),
                ),
                (
                    "level_3",
                    models.TextField(
                        blank=True, null=True, verbose_name="Organization Level 3"
                    ),
                ),
                ("url", models.URLField(blank=True, null=True, verbose_name="url")),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Logo"
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
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="location.location",
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
            name="InstitutionHistory",
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
                    "initial_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Initial Date"
                    ),
                ),
                (
                    "final_date",
                    models.DateField(blank=True, null=True, verbose_name="Final Date"),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="institution.institution",
                    ),
                ),
            ],
        ),
    ]
