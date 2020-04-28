from django.db import models

class Liga(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    f_creacion = models.DateField()
    presidente = models.CharField(max_length=40)

    class Meta:
        verbose_name="liga"
        verbose_name_plural="ligas"

    def __str__(self):
        return self.nombre

class Partidos(models.Model):
    fecha = models.DateField()
    equipo_local = models.CharField(max_length=40)
    equipo_visitante = models.CharField(max_length=40)
    goles = models.IntegerField()
    id_liga = models.ForeignKey(Liga, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name="partido"
        verbose_name_plural="partidos"


class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    presupuesto = models.IntegerField()
    presidente = models.CharField(max_length=40)
    estadio = models.CharField(max_length=40)
    titulos = models.IntegerField()
    id_liga = models.ForeignKey(Liga, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name="equipo"
        verbose_name_plural="equipos"

    def __str__(self):
        return self.nombre

class Juega(models.Model):
    id_equipo = models.ManyToManyField(Equipo)
    id_partido = models.ManyToManyField(Partidos)
    resultado = models.CharField(max_length=40)
    

    class Meta:
        verbose_name="juega"
        verbose_name_plural="juegas"

class Entrenador(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    pais = models.CharField(max_length=40)
    f_nacimiento = models.DateField()
    id_equipo = models.OneToOneField(Equipo, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name="entrenador"
        verbose_name_plural="entrenadores"

    def __str__(self):
        return self.nombre
    

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    pais = models.CharField(max_length=40)
    f_nacimiento = models.DateField()
    posicion = models.CharField(max_length=40)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.DO_NOTHING)
    id_entrenador = models.ForeignKey(Entrenador, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name="jugador"
        verbose_name_plural="jugadores"

    def __str__(self):
        return self.nombre
