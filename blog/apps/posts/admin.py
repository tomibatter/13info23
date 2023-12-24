from django.contrib import admin
from .models import Categoria, Post, Comentario

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'título', 'subtítulo', 'fecha', 'texto',
                    'activo', 'categoría', 'imagen', 'publicado')

admin.site.register(Categoria)

admin.site.register(Comentario)
