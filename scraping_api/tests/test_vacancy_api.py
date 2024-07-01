from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from scraping.models import Vacancy
from django.contrib.auth.models import User
from django.utils import timezone


class VacancyAPITests(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin = User.objects.create_superuser(username='admin', password='admin123', email='admin@example.com')

        self.vacancy = Vacancy.objects.create(
            url='http://example.com',
            title='Test Vacancy',
            company='Test Company',
            skills='Python, Django',
            primary_language=Vacancy.ProgrammingLanguages.PYTHON,
            created=timezone.now().date()
        )

    def test_list_vacancies(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_vacancy(self):
        url = reverse('post_list')
        data = {
            'url': 'http://newexample.com',
            'title': 'New Vacancy',
            'company': 'New Company',
            'skills': 'JavaScript, React',
            'primary_language': Vacancy.ProgrammingLanguages.JAVASCRIPT,
            'created': timezone.now().date().isoformat()
        }
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vacancy.objects.count(), 2)

    def test_retrieve_vacancy(self):
        url = reverse('post_detail', args=[self.vacancy.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Vacancy')

    def test_update_vacancy(self):
        url = reverse('post_detail', args=[self.vacancy.id])
        data = {'title': 'Updated Vacancy'}
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vacancy.objects.get(id=self.vacancy.id).title, 'Updated Vacancy')

    def test_delete_vacancy(self):
        url = reverse('post_detail', args=[self.vacancy.id])
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vacancy.objects.count(), 0)

    def test_non_admin_cannot_create_vacancy(self):
        url = reverse('post_list')
        data = {
            'url': 'http://newexample.com',
            'title': 'New Vacancy',
            'company': 'New Company',
            'skills': 'JavaScript, React',
            'primary_language': Vacancy.ProgrammingLanguages.JAVASCRIPT,
            'created': timezone.now().date().isoformat()
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_pagination(self):
        for i in range(25):
            Vacancy.objects.create(
                url=f'http://example{i}.com',
                title=f'Vacancy {i}',
                company=f'Company {i}',
                skills='Python',
                primary_language=Vacancy.ProgrammingLanguages.PYTHON,
                created=timezone.now().date()
            )

        url = reverse('post_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20)
        self.assertIsNotNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
