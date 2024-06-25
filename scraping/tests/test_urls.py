from django.test import SimpleTestCase
from django.urls import reverse, resolve
from scraping import views


class UrlsTest(SimpleTestCase):
    def test_jobs_view_url(self):
        url = reverse('jobs-view')
        self.assertEqual(url, '/')
        self.assertEqual(resolve(url).func.view_class, views.JobsView)

    def test_save_vacancy_url(self):
        url = reverse('save_vacancy', args=[1])
        self.assertEqual(url, '/save_vacancy/1/')
        self.assertEqual(resolve(url).func.view_class, views.SaveVacancyView)

    def test_favorite_vacancy_url(self):
        url = reverse('favorite-vacancy')
        self.assertEqual(url, '/favorite_vacancy/')
        self.assertEqual(resolve(url).func.view_class, views.FavoriteVacancyView)
