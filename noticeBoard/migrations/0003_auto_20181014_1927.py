# Generated by Django 2.1.2 on 2018-10-14 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticeBoard', '0002_auto_20170924_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
