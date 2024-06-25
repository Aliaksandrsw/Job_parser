from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from scraping.models import Vacancy, FavoriteVacancy


class VacancyModelTest(TestCase):
    def setUp(self):
        self.vacancy_data = {
            'url': 'https://example.com/job',
            'title': 'Python Developer',
            'company': 'Tech Corp',
            'skills': 'Python, Django, REST',
            'primary_language': Vacancy.ProgrammingLanguages.PYTHON,
            'created': '2024-06-25'
        }
        self.vacancy = Vacancy.objects.create(**self.vacancy_data)

    def test_vacancy_creation(self):
        self.assertTrue(isinstance(self.vacancy, Vacancy))
        self.assertEqual(str(self.vacancy), 'Python Developer')

    def test_vacancy_unique_url(self):
        with self.assertRaises(IntegrityError):
            Vacancy.objects.create(**self.vacancy_data)

    def test_vacancy_programming_languages_choices(self):
        self.assertEqual(self.vacancy.primary_language, Vacancy.ProgrammingLanguages.PYTHON)

        self.vacancy.primary_language = Vacancy.ProgrammingLanguages.JAVASCRIPT
        self.vacancy.save()
        self.assertEqual(self.vacancy.primary_language, Vacancy.ProgrammingLanguages.JAVASCRIPT)

    def test_vacancy_ordering(self):
        Vacancy.objects.create(
            url='https://example.com/job2',
            title='Java Developer',
            company='Tech Corp',
            skills='Java, Spring',
            primary_language=Vacancy.ProgrammingLanguages.JAVA,
            created='2024-06-26'
        )
        vacancies = Vacancy.objects.all()
        self.assertEqual(vacancies[0].title, 'Java Developer')
        self.assertEqual(vacancies[1].title, 'Python Developer')


class FavoriteVacancyModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vacancy = Vacancy.objects.create(
            url='https://example.com/job',
            title='Python Developer',
            company='Tech Corp',
            skills='Python, Django, REST',
            primary_language=Vacancy.ProgrammingLanguages.PYTHON,
            created='2024-06-25'
        )
        self.favorite = FavoriteVacancy.objects.create(
            user=self.user,
            vacancy=self.vacancy
        )

    def test_favorite_vacancy_creation(self):
        self.assertTrue(isinstance(self.favorite, FavoriteVacancy))
        self.assertEqual(str(self.favorite), 'Python Developer')

    def test_favorite_vacancy_unique_together(self):
        with self.assertRaises(IntegrityError):
            FavoriteVacancy.objects.create(user=self.user, vacancy=self.vacancy)

    def test_favorite_vacancy_status_choices(self):
        self.assertEqual(self.favorite.status, FavoriteVacancy.Status.SENT)

        self.favorite.status = FavoriteVacancy.Status.ACCEPTED
        self.favorite.save()
        self.assertEqual(self.favorite.status, FavoriteVacancy.Status.ACCEPTED)

    def test_favorite_vacancy_cascade_delete(self):
        self.user.delete()
        self.assertEqual(FavoriteVacancy.objects.count(), 0)