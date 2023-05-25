# Generated by Django 4.1.4 on 2023-02-01 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_job_translated_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='translator',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_translator': True}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='translator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
