from django.shortcuts import render
from django.views.generic import ListView

from scraping.models import Vacancy


class JobsView(ListView):
    model = Vacancy
    template_name = 'job_parser/index.html'
    context_object_name = 'vacancies'
    paginate_by = 10

    def get_queryset(self):
        return Vacancy.objects.all()
