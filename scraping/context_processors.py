from .models import Vacancy


def job_count(request):
    return {
        'job_count': Vacancy.objects.count(),
    }
