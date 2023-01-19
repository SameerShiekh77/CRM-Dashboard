# Generated by Django 4.1.2 on 2023-01-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_name', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('bin_size', models.CharField(max_length=255, verbose_name='Bin Size')),
                ('bin_property', models.CharField(max_length=11, verbose_name='Bin Property')),
                ('empty_label', models.BooleanField(default=True, verbose_name='Empty Label')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('bar_code', models.CharField(max_length=255, verbose_name='Bar Code')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Bin Set',
                'verbose_name_plural': 'Bin Set',
                'db_table': 'binset',
                'ordering': ['bin_name'],
            },
        ),
    ]
