# Generated by Django 5.2.4 on 2025-07-19 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0003_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='actor',
        ),
        migrations.AddField(
            model_name='performance',
            name='actors',
            field=models.ManyToManyField(related_name='performances', to='theatre.actor'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.stage'),
        ),
    ]
