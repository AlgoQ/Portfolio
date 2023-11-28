# Generated by Django 4.2.7 on 2023-11-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('startYear', models.IntegerField()),
                ('endYear', models.IntegerField()),
                ('link', models.CharField(max_length=255)),
                ('tags', models.JSONField(verbose_name='tags')),
            ],
            options={
                'ordering': ('startYear',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=500)),
                ('tags', models.JSONField(verbose_name='tags')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]