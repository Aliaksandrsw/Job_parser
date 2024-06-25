from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Job_parser.settings')

app = Celery('scraping')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'parse_habr_vacancies_hourly': {
        'task': 'scraping.tasks.parse_job_vacancies',
        'schedule': crontab(minute='0', hour='*/12')
    },
    'parse_geekjob_vacancies_hourly': {
        'task': 'scraping.tasks.parse_geekjob_vacancies',
        'schedule': crontab(minute='0', hour='*/12')
    }
}

app.autodiscover_tasks()
