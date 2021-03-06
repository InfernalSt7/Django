# Generated by Django 3.0.4 on 2020-06-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0012_auto_20200610_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='empatados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ganados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='goles_a_favor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='goles_en_contra',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='jugados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='perdidos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='puntos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
