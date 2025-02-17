# Generated by Django 3.2.12 on 2022-08-09 18:52

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
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Package File')),
                ('signature', models.CharField(blank=True, max_length=32, null=True, verbose_name='Signature')),
                ('status', models.CharField(choices=[('submitted', 'Submetido'), ('enqueued-for-validation', 'Enqueued for validation'), ('validated-with-errors', 'Validated with errors'), ('validated-without-errors', 'Validated without errors'), ('rejected', 'Rejeitado'), ('accepted', 'Accepted'), ('scheduled-for-publication', 'Scheduled for publication'), ('published', 'Publicado')], default='enqueued-for-validation', max_length=32, verbose_name='Status')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='package_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'permissions': (('finish_deposit', 'Can finish deposit'),),
            },
        ),
        migrations.CreateModel(
            name='ValidationError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('package-file-error', 'PACKAGE_FILE_ERROR'), ('xml-format-error', 'XML_FORMAT_ERROR'), ('bibliometrics-data-error', 'BIBLIOMETRICS_DATA_ERROR'), ('services-data-error', 'SERVICES_DATA_ERROR'), ('data-consistency_error', 'DATA_CONSISTENCY_ERROR'), ('criteria-issues', 'CRITERIA_ISSUES')], max_length=32, verbose_name='Category')),
                ('row', models.PositiveIntegerField(blank=True, null=True, verbose_name='Row')),
                ('column', models.PositiveIntegerField(blank=True, null=True, verbose_name='Column')),
                ('message', models.CharField(blank=True, max_length=128, null=True, verbose_name='Message')),
                ('snippet', models.TextField(blank=True, max_length=255, null=True, verbose_name='Snippet')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.package')),
            ],
        ),
    ]
