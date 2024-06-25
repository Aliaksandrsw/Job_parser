from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from scraping.models import Vacancy, FavoriteVacancy
from scraping.views import JobsView, SaveVacancyView, FavoriteVacancyView


class JobsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vacancy = Vacancy.objects.create(
            url='https://example.com/job',  # Добавьте URL
            title='Test Job',
            company='Test Company',  # Добавьте компанию
            skills='Python, Django',  # Добавьте навыки
            primary_language=Vacancy.ProgrammingLanguages.PYTHON,
            created=timezone.now().date()  # Используйте текущую дату
        )

    def test_jobs_view_get(self):
        request = self.factory.get(reverse('jobs-view'))
        request.user = self.user
        response = JobsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('vacancies', response.context_data)
        self.assertIn('form', response.context_data)

    def test_jobs_view_search(self):
        request = self.factory.get(reverse('jobs-view'), {'query': 'Python'})
        request.user = self.user
        response = JobsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.vacancy, response.context_data['vacancies'])


class SaveVacancyViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vacancy = Vacancy.objects.create(
            url='https://example.com/job',
            title='Test Job',
            company='Test Company',
            skills='Python, Django',
            primary_language=Vacancy.ProgrammingLanguages.PYTHON,
            created=timezone.now().date()
        )

    def test_save_vacancy_view_post(self):
        request = self.factory.post(reverse('save_vacancy', args=[self.vacancy.id]))
        request.user = self.user
        response = SaveVacancyView.as_view()(request, vacancy_id=self.vacancy.id)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FavoriteVacancy.objects.filter(user=self.user, vacancy=self.vacancy).exists())


class FavoriteVacancyViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vacancy = Vacancy.objects.create(
            url='https://example.com/job',
            title='Test Job',
            company='Test Company',
            skills='Python, Django',
            primary_language=Vacancy.ProgrammingLanguages.PYTHON,
            created=timezone.now().date()
        )
        self.favorite = FavoriteVacancy.objects.create(
            user=self.user,
            vacancy=self.vacancy,
            status=FavoriteVacancy.Status.SENT
        )

    def test_favorite_vacancy_view_get(self):
        request = self.factory.get(reverse('favorite-vacancy'))
        request.user = self.user
        response = FavoriteVacancyView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('favorite_vacancy', response.context_data)
        self.assertIn('form', response.context_data)

    def test_favorite_vacancy_view_post(self):
        form_data = {'status': FavoriteVacancy.Status.ACCEPTED}
        request = self.factory.post(reverse('favorite-vacancy'), data=form_data)
        request.user = self.user
        request.POST = request.POST.copy()
        request.POST['favorite_id'] = self.favorite.id
        response = FavoriteVacancyView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.favorite.refresh_from_db()
        self.assertEqual(self.favorite.status, FavoriteVacancy.Status.ACCEPTED)
