# Generated by Django 3.2.15 on 2022-09-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('site', models.URLField(blank=True, max_length=500, null=True)),
                ('uname_site', models.CharField(blank=True, max_length=500, null=True)),
                ('pass_site', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]