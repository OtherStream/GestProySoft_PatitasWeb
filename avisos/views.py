# avisos/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Para proteger las vistas

from .models import Publicacion
from .forms import PublicacionForm

# Mixin de protección: Asegúrate de que el usuario esté logueado
class StaffRequiredMixin(LoginRequiredMixin):
    # Aquí puedes añadir lógica para verificar si el usuario es staff si es necesario
    pass

## VISTAS PARA EL CRUD DE PUBLICACIONES

# 1. LISTAR
class PublicacionListView(StaffRequiredMixin, ListView):
    model = Publicacion
    template_name = 'avisos/publicacion_list.html' 
    context_object_name = 'publicaciones'

# 2. CREAR
class PublicacionCreateView(StaffRequiredMixin, CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'avisos/publicacion_form.html' 
    success_url = reverse_lazy('publicacion_list')

# 3. EDITAR
class PublicacionUpdateView(StaffRequiredMixin, UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'avisos/publicacion_form.html'
    success_url = reverse_lazy('publicacion_list')

# 4. ELIMINAR
class PublicacionDeleteView(StaffRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'avisos/publicacion_confirm_delete.html' 
    success_url = reverse_lazy('publicacion_list')