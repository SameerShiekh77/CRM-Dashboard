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
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_supplier', models.CharField(max_length=255, verbose_name='Goods Supplier')),
                ('goods_weight', models.FloatField(default=0, verbose_name='Goods Weight')),
                ('goods_w', models.FloatField(default=0, verbose_name='Goods Width')),
                ('goods_d', models.FloatField(default=0, verbose_name='Goods Depth')),
                ('goods_h', models.FloatField(default=0, verbose_name='Goods Height')),
                ('unit_volume', models.FloatField(default=0, verbose_name='Unit Volume')),
                ('goods_unit', models.CharField(max_length=255, verbose_name='Goods Unit')),
                ('goods_class', models.CharField(max_length=255, verbose_name='Goods Class')),
                ('goods_brand', models.CharField(max_length=255, verbose_name='Goods Brand')),
                ('goods_color', models.CharField(max_length=255, verbose_name='Goods Color')),
                ('goods_shape', models.CharField(max_length=255, verbose_name='Goods Shape')),
                ('goods_specs', models.CharField(max_length=255, verbose_name='Goods Specs')),
                ('goods_origin', models.CharField(max_length=255, verbose_name='Goods Origin')),
                ('safety_stock', models.BigIntegerField(default=0, verbose_name='Goods Safety Stock')),
                ('goods_cost', models.FloatField(default=0, verbose_name='Goods Cost')),
                ('goods_price', models.FloatField(default=0, verbose_name='Goods Price')),
                ('creater', models.CharField(max_length=255, verbose_name='Who created')),
                ('bar_code', models.CharField(max_length=255, verbose_name='Bar Code')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Goods List',
                'verbose_name_plural': 'Goods List',
                'db_table': 'goods',
                'ordering': ['-id'],
            },
        ),
    ]
