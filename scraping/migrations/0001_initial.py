# Generated by Django 5.0.6 on 2024-06-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('company', models.CharField(max_length=250, verbose_name='Компания')),
                ('skills', models.TextField()),
                ('primary_language', models.CharField(choices=[('python', 'Python'), ('javascript', 'JavaScript'), ('ruby', 'Ruby'), ('csharp', 'C#'), ('java', 'Java')], default='python', max_length=20)),
                ('created', models.CharField(max_length=100, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-created'],
            },
        ),
    ]
