import dateparser
from celery import shared_task
from datetime import datetime
from .par.habr_parser import *
from .models import Vacancy


@shared_task
def parse_job_vacancies():
    url_lst = habr_get_all_url()
    vacancy_data_list = habr_get_content(url_lst)

    for vacancy_data in vacancy_data_list:
        created_date = dateparser.parse(vacancy_data['created']).date()
        vacancy, created = Vacancy.objects.get_or_create(
            url=vacancy_data['url'],
            defaults={
                'title': vacancy_data['title'],
                'company': vacancy_data['company'],
                'skills': vacancy_data['skills'],
                'created': created_date,
            }
        )


