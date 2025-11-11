# avisos/models.py

from django.db import models
from django.utils import timezone

# Opciones para el campo de tipo de publicación (el combobox)
TIPO_PUBLICACION = [
    ('AVISO', 'Aviso'),
    ('NOTICIA', 'Noticia'),
    ('OTRO', 'Otro'),
]

class Publicacion(models.Model):
    # El "Nombre" o "Título" de la publicación
    nombre = models.CharField(max_length=200, verbose_name='Título/Nombre') 
    
    # Campo para el combobox: Almacena el código (AVISO, NOTICIA, OTRO)
    tipo = models.CharField(
        max_length=10, 
        choices=TIPO_PUBLICACION, 
        default='AVISO', 
        verbose_name='Tipo de Publicación'
    )
    
    # La descripción larga
    descripcion = models.TextField(verbose_name='Descripción')
    
    # Campo de imagen (se almacena en MEDIA_ROOT/publicaciones/)
    imagen = models.ImageField(upload_to='publicaciones', null=True, blank=True, verbose_name='Imagen')
    
    # Fecha de creación (se establece automáticamente al crear la publicación)
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones (Avisos/Servicios)'
        ordering = ['-fecha_creacion'] # Ordenar por la más reciente primero

    def __str__(self):
        return self.nombre