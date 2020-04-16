# Generated by Django 3.0.5 on 2020-04-16 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shavershan', '0005_confirmed_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmed_order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
