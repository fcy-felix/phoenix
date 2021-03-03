# Generated by Django 3.1.3 on 2021-03-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210302_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.CharField(max_length=64, verbose_name='拥有者'),
        ),
        migrations.AlterField(
            model_name='articleclassify',
            name='creator',
            field=models.CharField(max_length=64, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='articleclassify',
            name='owner',
            field=models.CharField(max_length=64, verbose_name='拥有者'),
        ),
        migrations.AlterField(
            model_name='articleserial',
            name='creator',
            field=models.CharField(max_length=64, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='articleserial',
            name='owner',
            field=models.CharField(max_length=64, verbose_name='拥有者'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='creator',
            field=models.CharField(max_length=64, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='owner',
            field=models.CharField(max_length=64, verbose_name='拥有者'),
        ),
    ]
