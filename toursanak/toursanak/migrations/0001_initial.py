# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 12:32
from __future__ import unicode_literals

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
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=130)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagename', models.ImageField(upload_to=b'static/images/albums/')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TabDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Tab')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(db_index=True)),
                ('feature_image', models.ImageField(upload_to=b'static/images/feature_image/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to=b'static/images/banner/')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('Short_description', models.CharField(db_index=True, max_length=200)),
                ('description', models.TextField(blank=True, db_index=True, null=True)),
                ('keywords', models.TextField(blank=True, db_index=True, null=True)),
                ('map', models.TextField(blank=True, null=True)),
                ('published_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Category')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tab',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Tour'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Tour'),
        ),
        migrations.AddField(
            model_name='image',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Tour'),
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Schedule'),
        ),
        migrations.AddField(
            model_name='booking',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toursanak.Tour'),
        ),
    ]