# Generated by Django 3.0.6 on 2022-08-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFamily', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='familiaSec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fechaNac', models.DateField()),
            ],
        ),
    ]
