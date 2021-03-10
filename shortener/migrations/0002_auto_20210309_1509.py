# Generated by Django 3.0.13 on 2021-03-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='designed_link',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Designed Link'),
        ),
        migrations.AlterField(
            model_name='link',
            name='short_link',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Short_link'),
        ),
    ]