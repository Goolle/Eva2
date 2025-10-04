from django.contrib import admin

# Register your models here.
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_creacion', 'fecha_limite')
    list_filter = ('vigente', 'prioridad', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)