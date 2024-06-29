from rest_framework import serializers

from scraping.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['url', 'title', 'company', 'skills']
