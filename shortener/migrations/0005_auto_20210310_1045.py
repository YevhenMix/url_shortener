# Generated by Django 3.0.13 on 2021-03-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20210310_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='designed_link',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Designed Link'),
        ),
    ]