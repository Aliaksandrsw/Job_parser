from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsView.as_view(), name='jobs-view'),
]
