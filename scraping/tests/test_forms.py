from django import forms
from django.test import TestCase

from scraping.forms import FavoriteStatusForm, SearchForm
from scraping.models import FavoriteVacancy


class FavoriteStatusFormTest(TestCase):
    def test_favorite_status_form_fields(self):
        form = FavoriteStatusForm()
        self.assertEqual(list(form.fields.keys()), ['status'])

    def test_favorite_status_form_widget(self):
        form = FavoriteStatusForm()
        self.assertIsInstance(form.fields['status'].widget, forms.Select)
        self.assertEqual(form.fields['status'].widget.attrs['class'], 'form-select form-select-sm')

    def test_favorite_status_form_model(self):
        form = FavoriteStatusForm()
        self.assertEqual(form._meta.model, FavoriteVacancy)


class SearchFormTest(TestCase):
    def test_search_form_fields(self):
        form = SearchForm()
        self.assertEqual(list(form.fields.keys()), ['query'])

    def test_search_form_query_field(self):
        form = SearchForm()
        self.assertIsInstance(form.fields['query'], forms.CharField)
