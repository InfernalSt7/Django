# Generated by Django 3.0.4 on 2020-06-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0008_auto_20200524_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='empatados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ganados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='goles_a_favor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='goles_en_contra',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='jugados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipo',
            name='perdidos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jugador',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
