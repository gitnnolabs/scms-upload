# Generated by Django 1.11.7 on 2018-03-22 16:32
from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0005_add_solarschedule_events_choices'),
        # ('django_celery_beat', '0006_auto_20180210_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crontabschedule',
            options={
                'ordering': [
                    'month_of_year', 'day_of_month',
                    'day_of_week', 'hour', 'minute', 'timezone'
                ],
                'verbose_name': 'crontab',
                'verbose_name_plural': 'crontabs'
            },
        ),
        migrations.AddField(
            model_name='crontabschedule',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='UTC'),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='day_of_month',
            field=models.CharField(
                default='*', max_length=124, verbose_name='day of month'
            ),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='hour',
            field=models.CharField(
                default='*', max_length=96, verbose_name='hour'
            ),
        ),
        migrations.AlterField(
            model_name='crontabschedule',
            name='minute',
            field=models.CharField(
                default='*', max_length=240, verbose_name='minute'
            ),
        ),
    ]
