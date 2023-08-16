# Generated by Django 4.2.3 on 2023-08-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acciones', '0002_compraaccion_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='ETF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('subyacente', models.CharField(max_length=100)),
                ('precio_a_comprar', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
