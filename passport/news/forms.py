from .models import Articles
from django.forms import ModelForm, TextInput, NumberInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['troad', 'nroad', 'n_km', 'k_km']

        widgets = {
            "troad": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Титул дороги'
            }),
            "nroad": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование дороги'
            }),
            "n_km": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начало дороги, км',
                'decimal_places': 3
            }),
            "k_km": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Конец дороги, км',
                'decimal_places': 3
            }),
        }
