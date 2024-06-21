from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobsView.as_view(), name='jobs-view'),
    path('save_vacancy/<int:vacancy_id>/', views.SaveVacancyView.as_view(), name='save_vacancy'),
    path('favorite_vacancy/', views.FavoriteVacancyView.as_view(), name='favorite-vacancy')
]
