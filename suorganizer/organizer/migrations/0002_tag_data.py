"""
User created migration file that will initialize the database with
tag information, instead of starting with an empty database.
"""
from django.db import migrations


TAGS = (
    # (tag name, tag slug),
    ('augmented reality', 'augmented-reality'),
    ("big data", "big-data"),
    ("django", "django"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("mobile", "mobile"),
    ("node.js", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
    ("self improvement", "self-improvement"),
    ("video games", "video-games"),
    ("web", "web"),
    ("zend", "zend"),
)


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')    # Fetches the historical model of Tag (instead of importing it)
    for tag_name, tag_slug in TAGS:
        Tag.objects.create(name=tag_name, slug=tag_slug)


def remove_tag_date(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')  # Fetches the historical model of Tag (instead of importing it)
    for _, tag_slug in TAGS:
        tag = Tag.objects.get(slug=tag_slug)
        tag.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_tag_data, remove_tag_date)
    ]
