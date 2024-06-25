from django import forms
from .models import FavoriteVacancy


class FavoriteStatusForm(forms.ModelForm):
    class Meta:
        model = FavoriteVacancy
        fields = ['status']
        widgets = {
             'status': forms.Select(attrs={'class': 'form-select form-select-sm'})
        }


class SearchForm(forms.Form):
    query = forms.CharField()