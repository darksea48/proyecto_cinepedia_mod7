from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    fecha_estreno = models.DateField()
    sinopsis = models.TextField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    pelicula = models.ForeignKey(Pelicula, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fijado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fijado', '-fecha'] # Por defecto, se ordenan los comentarios por fecha descendente
    
    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.pelicula.nombre}"