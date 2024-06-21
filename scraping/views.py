from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from scraping.models import Vacancy, FavoriteVacancy


class JobsView(ListView):
    model = Vacancy
    template_name = 'job_parser/index.html'
    context_object_name = 'vacancies'
    paginate_by = 10

    def get_queryset(self):
        return Vacancy.objects.all().order_by('-created')


class SaveVacancyView(LoginRequiredMixin, View):
    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        user = request.user
        FavoriteVacancy.objects.get_or_create(user=user, vacancy=vacancy)
        return redirect('jobs-view')


class FavoriteVacancyView(LoginRequiredMixin, ListView):
    model = FavoriteVacancy
    template_name = 'job_parser/favoritevacancy.html'
    context_object_name = 'favorite_vacancy'
    paginate_by = 10

    def get_queryset(self):
        return FavoriteVacancy.objects.filter(user=self.request.user)
