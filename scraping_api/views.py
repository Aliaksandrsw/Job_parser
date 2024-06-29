from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from scraping.models import Vacancy
from scraping_api.permissions import IsAdminOrReadOnly
from scraping_api.serializers import VacancySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostList(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = StandardResultsSetPagination


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = VacancySerializer
