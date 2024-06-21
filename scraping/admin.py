from django.contrib import admin
from django.utils.html import format_html

from .models import Vacancy, FavoriteVacancy


@admin.register(Vacancy)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteVacancy)
class FavoriteVacancyAdmin(admin.ModelAdmin):
    readonly_fields = ['get_vacancy_url']
    fields = ['user', 'vacancy', 'status', 'get_vacancy_url']
    list_display = ['user', 'vacancy', 'status', 'get_vacancy_url']
    list_filter = ['status']
    search_fields = ['user__username', 'vacancy__title']

    def get_vacancy_url(self, obj):
        url = obj.vacancy.url
        return format_html('<a href="{}" target="_blank">{}</a>', url, url)

    get_vacancy_url.short_description = 'Vacancy URL'
