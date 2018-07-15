from django.db import models
from django.contrib.auth.models import User

def custom_upload_to(instance, filename):
    old_instance = Newsfeed.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'newsfeed/' + filename

# Create your models here.
class Newsfeed(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título", unique=True)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="newsfeed", verbose_name="Imagen", blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created', 'updated']
    def __str__(self):
        return self.title