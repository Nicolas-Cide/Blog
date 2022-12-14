# Generated by Django 3.0.6 on 2022-08-25 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appFamily', '0005_clientes_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email o Gmail'),
        ),
    ]
