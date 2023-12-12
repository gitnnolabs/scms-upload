# Generated by Django 4.2.6 on 2023-12-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("doi", "0001_initial"),
        ("researcher", "0001_initial"),
        ("package", "0001_initial"),
        ("journal", "0001_initial"),
        ("issue", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                    "pid_v3",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="PID v3"
                    ),
                ),
                (
                    "article_type",
                    models.CharField(
                        choices=[
                            ("abstract", "Abstract"),
                            ("addendum", "Addendum"),
                            ("announcement", "Announcement"),
                            ("article-commentary", "Article-Commentary"),
                            ("book-review", "Book-Review"),
                            ("books-received", "Books-Received"),
                            ("brief-report", "Brief-Report"),
                            ("calendar", "Calendar"),
                            ("case-report", "Case-Report"),
                            ("clinical-trial", "Clinical-Trial"),
                            ("collection", "Coleção"),
                            ("correction", "Correction"),
                            ("data-article", "Data-Article"),
                            ("discussion", "Discussion"),
                            ("dissertation", "Dissertation"),
                            ("editorial", "Editorial"),
                            ("editorial-material", "Editorial-Material"),
                            ("guideline", "Guideline"),
                            ("in-brief", "In-Brief"),
                            ("interview", "Interview"),
                            ("introduction", "Introduction"),
                            ("letter", "Letter"),
                            ("meeting-report", "Meeting-Report"),
                            ("news", "News"),
                            ("obituary", "Obituary"),
                            ("oration", "Oration"),
                            ("other", "Other"),
                            ("partial-retraction", "Partial-Retraction"),
                            ("product-review", "Product-Review"),
                            ("rapid-communication", "Rapid-Communication"),
                            ("reply", "Reply"),
                            ("reprint", "Reprint"),
                            ("research-article", "Research-Article"),
                            ("retraction", "Retraction"),
                            ("review-article", "Review-Article"),
                            ("technical-report", "Technical-Report"),
                            ("translation", "Translation"),
                        ],
                        max_length=32,
                        verbose_name="Article type",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("change-submitted", "Change submitted"),
                            ("required-update", "Required update"),
                            ("required-erratum", "Required erratum"),
                            ("read-to-publish", "Ready to publish"),
                            ("scheduled-to-publish", "Scheduled to publish"),
                            ("published", "Publicado"),
                        ],
                        max_length=32,
                        null=True,
                        verbose_name="Article status",
                    ),
                ),
                (
                    "elocation_id",
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        verbose_name="Elocation ID",
                    ),
                ),
                (
                    "fpage",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="First page"
                    ),
                ),
                (
                    "lpage",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="Last page"
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
                    "issue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="issue.issue",
                    ),
                ),
                (
                    "journal",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="journal.journal",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("make_article_change", "Can make article change"),
                    ("request_article_change", "Can request article change"),
                ),
            },
        ),
        migrations.CreateModel(
            name="RequestArticleChange",
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
                ("deadline", models.DateField(verbose_name="Deadline")),
                (
                    "change_type",
                    models.CharField(
                        choices=[("update", "Atualizar"), ("erratum", "Erratum")],
                        max_length=32,
                        verbose_name="Change type",
                    ),
                ),
                (
                    "comment",
                    wagtail.fields.RichTextField(
                        blank=True, max_length=512, null=True, verbose_name="Comment"
                    ),
                ),
                (
                    "pid_v3",
                    models.CharField(
                        blank=True, max_length=23, null=True, verbose_name="PID v3"
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="article.article",
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
                    "demanded_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
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
            name="RelatedItem",
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
                    "item_type",
                    models.CharField(
                        choices=[
                            ("addendum", "Addendum"),
                            ("commentary-article", "Commentary article"),
                            ("corrected-article", "Corrected article"),
                            ("letter", "Letter"),
                            ("partial-retraction", "Partial retraction"),
                            ("retracted-article", "Retracted article"),
                        ],
                        max_length=32,
                        verbose_name="Related item type",
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
                    "source_article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_article",
                        to="article.article",
                    ),
                ),
                (
                    "target_article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target_article",
                        to="article.article",
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
            name="ArticleTitle",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
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
                ("title", models.TextField(verbose_name="Title")),
                ("lang", models.CharField(max_length=64, verbose_name="Language")),
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
                    "title_with_lang",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="title_with_lang",
                        to="article.article",
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
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ArticleDOIWithLang",
            fields=[
                (
                    "doiwithlang_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="doi.doiwithlang",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "doi_with_lang",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doi_with_lang",
                        to="article.article",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("doi.doiwithlang", models.Model),
        ),
        migrations.CreateModel(
            name="ArticleAuthor",
            fields=[
                (
                    "researcher_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="researcher.researcher",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "author",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to="article.article",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("researcher.researcher", models.Model),
        ),
        migrations.AddField(
            model_name="article",
            name="related_items",
            field=models.ManyToManyField(
                related_name="related_to",
                through="article.RelatedItem",
                to="article.article",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="sps_pkg",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="package.spspkg",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_last_mod_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updater",
            ),
        ),
    ]
