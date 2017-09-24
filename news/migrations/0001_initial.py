# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 04:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.wagtailcore.fields
import wagtail.wagtailsearch.index
import wagtailnews.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('nav_text', models.TextField(help_text='The text that appears in the navigation element', verbose_name='Navigation Text')),
            ],
            bases=(wagtailnews.models.NewsIndexMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published date')),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='Live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='Has unpublished changes')),
                ('title', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('newsindex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
            options={
                'ordering': ('-date',),
                'abstract': False,
            },
            bases=(wagtail.wagtailsearch.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='NewsItemRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('content_json', models.TextField(verbose_name='Content JSON')),
                ('newsitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='news.NewsItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'news item revision',
                'abstract': False,
            },
        ),
    ]
