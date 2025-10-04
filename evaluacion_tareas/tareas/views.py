from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'
    context_object_name = 'tareas'

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'

class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'fecha_limite']
    success_url = reverse_lazy('tareas:list')

class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    success_url = reverse_lazy('tareas:list')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:list')
