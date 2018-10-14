# Generated by Django 2.1.2 on 2018-10-14 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workshopfeedback',
            name='workshop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='workshop.Workshop'),
        ),
    ]
