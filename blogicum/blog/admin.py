from django.contrib import admin

from .models import Category, Location, Post, Comment

# Интерфейс для категорий
admin.site.register(Category)
# Интерфейс для комментариев
admin.site.register(Comment)
# Интерфейс для локаций
admin.site.register(Location)
# Интерфейс для постов
admin.site.register(Post)
