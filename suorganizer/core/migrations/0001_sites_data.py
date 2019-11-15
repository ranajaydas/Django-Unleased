"""
Don't make all this for a real project without understanding what's going on.
Potential side effects - will fuck up the password reset email links.
"""

from django.conf import settings
from django.db import migrations, models


def add_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    new_domain = '127.0.0.1:8000'
    new_name = 'Startup Organizer'
    site_id = getattr(settings, 'SITE_ID', 1)
    if Site.objects.exists():
        current_site = Site.objects.get(pk=site_id)
        current_site.domain = new_domain
        current_site.name = new_name
        current_site.save()
    else:
        current_site = Site(
            pk=site_id,  # coerce primary key
            domain=new_domain,
            name=new_name)
        current_site.save()


def remove_site_data(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    current_site = Site.objects.get(pk=getattr(settings, 'SITE_ID', 1))
    current_site.domain = '127.0.0.1:8000'
    current_site.name = 'Startup Organizer'
    current_site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_site_data, remove_site_data),
    ]
