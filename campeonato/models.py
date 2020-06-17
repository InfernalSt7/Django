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


class Equipo(models.Model):
    foto = models.ImageField(blank = True, upload_to = "media")
    nombre = models.CharField(max_length=40)
    presupuesto = models.IntegerField()
    presidente = models.CharField(max_length=40)
    estadio = models.CharField(max_length=40)
    titulos = models.IntegerField()
    id_liga = models.ForeignKey(Liga, on_delete=models.SET_NULL, null=True, blank=True)
    puntos = models.IntegerField(default = 0, null=True, blank=True)
    jugados = models.IntegerField(default = 0, null=True, blank=True)
    ganados = models.IntegerField(default = 0, null=True, blank=True)
    empatados = models.IntegerField(default = 0, null=True, blank=True)
    perdidos = models.IntegerField(default = 0, null=True, blank=True)
    goles_a_favor = models.IntegerField(default = 0, null=True, blank=True)
    goles_en_contra = models.IntegerField(default = 0, null=True, blank=True)
    class Meta:
        verbose_name="equipo"
        verbose_name_plural="equipos"
        ordering = ['-puntos']
    def __str__(self):
        return self.nombre

class Partidos(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete = models.SET_NULL, null=True, blank=True, max_length=40, related_name="equipo_local")
    equipo_visitante = models.ForeignKey(Equipo, on_delete = models.SET_NULL, null=True, blank=True, max_length=40, 
    related_name="equipo_visitante")
    goles = models.IntegerField()
    id_liga = models.ForeignKey(Liga, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name="partido"
        verbose_name_plural="partidos"



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
    id_equipo = models.OneToOneField(Equipo, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name="entrenador"
        verbose_name_plural="entrenadores"

    def __str__(self):
        return self.nombre
    

class Jugador(models.Model):
    foto = models.ImageField(blank = True, upload_to = "media")
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    pais = models.CharField(max_length=40)
    f_nacimiento = models.DateField()
    posicion = models.CharField(max_length=40)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name="jugador"
        verbose_name_plural="jugadores"

    def __str__(self):
        return self.nombre
   