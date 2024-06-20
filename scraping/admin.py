from django.contrib import admin

from .models import Vacancy, FavoriteVacancy


@admin.register(Vacancy)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteVacancy)
class FavoriteVacancyAdmin(admin.ModelAdmin):
    list_display = ['user', 'vacancy', 'status']
    list_filter = ['status']
    search_fields = ['user__username', 'vacancy__title']