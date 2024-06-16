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