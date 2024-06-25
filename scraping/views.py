from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from scraping.forms import FavoriteStatusForm, SearchForm
from scraping.models import Vacancy, FavoriteVacancy


class JobsView(ListView):
    model = Vacancy
    template_name = 'job_parser/index.html'
    context_object_name = 'vacancies'
    paginate_by = 10

    def get_queryset(self):
        queryset = Vacancy.objects.all().order_by('-created')
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                queryset = queryset.annotate(
                    search=SearchVector('skills'),
                ).filter(search=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        if self.request.user.is_authenticated:
            favorite_vacancies = FavoriteVacancy.objects.filter(user=self.request.user).values_list('vacancy_id',
                                                                                                    flat=True)
            context['favorite_vacancies'] = favorite_vacancies
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FavoriteStatusForm()
        return context

    def post(self, request, *args, **kwargs):
        favorite_id = request.POST.get('favorite_id')
        favorite = FavoriteVacancy.objects.get(id=favorite_id, user=request.user)
        form = FavoriteStatusForm(request.POST, instance=favorite)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('favorite-vacancy'))
