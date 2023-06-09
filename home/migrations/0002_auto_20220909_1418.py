# Generated by Django 3.2.15 on 2022-09-09 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='name',
        ),
        migrations.AddField(
            model_name='password',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='password',
            name='u_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='u_name', to='auth.user'),
            preserve_default=False,
        ),
    ]
