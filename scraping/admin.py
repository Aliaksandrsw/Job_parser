from django.contrib import admin

from .models import Vacancy


@admin.register(Vacancy)
class PostAdmin(admin.ModelAdmin):
    pass

