# Generated by Django 4.2.3 on 2023-07-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_acompanhamento_bebidas_extra_sobremesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompanhamento',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='extra',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sobremesa',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
    ]
