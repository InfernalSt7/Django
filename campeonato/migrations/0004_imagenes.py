# Generated by Django 3.0.4 on 2020-05-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0003_equipo_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]