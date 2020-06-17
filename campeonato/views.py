from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from campeonato.models import *
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from .forms import *
   
class Lista_Index(ListView):
    template_name = 'index.html'
    model = Juega
    paginate_by = 6

class Contactos(TemplateView):
    template_name = 'contactos.html'
# def contactos(request):
#     return render(request, 'contactos.html')

class Lista_Resultados(ListView):
    template_name = 'resultados.html'
    model = Juega
    paginate_by = 5     

def champions(request):
    return render(request, 'internacional/champions.html')

class Clasificacion_Champions(ListView):
    template_name = 'internacional/clasificacion_champions.html'
    model = Equipo
    paginate_by = 20
    # def get(self, request, *args, **kwargs):
    #     equipos = Equipo.objects.order_by('-puntos')
    #     context = {'equipos': equipos}
    #     return render(request, self.template_name, context)

def clasificacion(request, id):
    liga = get_object_or_404(Liga, id = id)
    equipos = Equipo.objects.filter(id_liga = liga).order_by('-puntos')
    context = {'equipos': equipos}
    return render(request, 'liga/clasificacion.html', context)

def club(request, id):
    club = get_object_or_404(Equipo, id= id)
    jugadores = Jugador.objects.filter(id_equipo = id)
    entrenadores = Entrenador.objects.filter(id_equipo = id)
    context = {'club': club, 'jugadores': jugadores, 'entrenadores': entrenadores}
    return render(request, 'club.html', context)    

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('campeonato:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)

    return HttpResponseRedirect('/login/')

class AddJugador(CreateView):
    model = Jugador
    form_class= JugadorForm
    template_name = 'crud/addJugador.html'
    success_url = reverse_lazy('campeonato:index')

class AddEquipo(CreateView):
    model = Equipo
    form_class= EquipoForm
    template_name = 'crud/addEquipo.html'
    success_url = reverse_lazy('campeonato:index')

def eliminarEquipo(request, id):
    equipo = Equipo.objects.get(id = id)
    equipo.delete()
    return redirect('campeonato:index')

def eliminarJugador(request, id):
    jugador = Jugador.objects.get(id = id)
    jugador.delete()
    return redirect('campeonato:index')

class EditEquipo(UpdateView):
    model = Equipo
    form_class= EquipoForm
    template_name = 'crud/addEquipo.html'
    success_url = reverse_lazy('campeonato:index')

class EditJugador(UpdateView):
    model = Jugador
    form_class= JugadorForm
    template_name = 'crud/addJugador.html'
    success_url = reverse_lazy('campeonato:index')