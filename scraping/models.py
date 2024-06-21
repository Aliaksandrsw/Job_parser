from django.contrib.auth import get_user_model
from django.db import models


class Vacancy(models.Model):
    class ProgrammingLanguages(models.TextChoices):
        PYTHON = 'python', 'Python'
        JAVASCRIPT = 'javascript', 'JavaScript'
        RUBY = 'ruby', 'Ruby'
        CSHARP = 'csharp', 'C#'
        JAVA = 'java', 'Java'

    url = models.URLField(unique=True, verbose_name='URL')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    company = models.CharField(max_length=250, verbose_name='Компания')
    skills = models.TextField()
    primary_language = models.CharField(
        max_length=20,
        choices=ProgrammingLanguages.choices,
        default=ProgrammingLanguages.PYTHON,
    )
    created = models.CharField(max_length=100, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created']

    def __str__(self):
        return self.title


class FavoriteVacancy(models.Model):
    class Status(models.TextChoices):
        SENT = 'Отправлено', 'Отправлено'
        REJECTED = 'Отказ', 'Отказ'
        ACCEPTED = 'Принято', 'Принято'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Вакансия')
    status = models.CharField(
        choices=Status.choices,
        default=Status.SENT,
        verbose_name='Статус'
    )

    class Meta:
        unique_together = ('user', 'vacancy')
        verbose_name = 'Избранная вакансия'
        verbose_name_plural = 'Избранные вакансии'

    def __str__(self):
        return self.vacancy.title
