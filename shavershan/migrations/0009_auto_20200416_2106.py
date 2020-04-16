# Generated by Django 3.0.5 on 2020-04-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shavershan', '0008_order_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmed_order',
            name='order',
        ),
        migrations.AddField(
            model_name='confirmed_order',
            name='order',
            field=models.ManyToManyField(to='shavershan.order'),
        ),
    ]
