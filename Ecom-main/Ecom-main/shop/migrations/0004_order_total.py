# Generated by Django 3.2.4 on 2021-07-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210711_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
