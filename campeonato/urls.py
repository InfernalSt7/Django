from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(Lista_Index.as_view()), name = 'index'),
    path('contacts/', Contactos, name = 'contactos'),
    path('resultados/', Lista_Resultados.as_view(), name = 'resultados'),
    path('liga/<int:id>', clasificacion, name='clasificacion'),
    path('champions/', champions, name = 'champions'),
    path('champions/clasificacion/', Clasificacion_Champions.as_view(), name='clasificacion_champions'),
    path('club/<int:id>', club, name='detail_club'),
    path('addEquipo', AddEquipo.as_view(), name='addEquipo'),
    path('eliminarEquipo/<int:id>', eliminarEquipo, name='deleteEquipo'),
    path('eliminarJugador/<int:id>', eliminarJugador, name='deleteJugador'),
    path('addJugador', AddJugador.as_view(), name='addJugador'),
    path('editEquipo/<int:pk>', EditEquipo.as_view(), name='editEquipo'),
    path('editJugador/<int:pk>', EditJugador.as_view(), name='editJugador'),
] 