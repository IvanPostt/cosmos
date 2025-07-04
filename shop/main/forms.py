from django import forms

from .models import Category, SpaceObj


class AddForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрано', widget=forms.Select(attrs={'class': 'form-input'}))
    class Meta:
        model = SpaceObj
        fields = ['title', 'slug', 'description', 'category', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 6, 'class': "form-input"}),
            'file': forms.FileInput(attrs={'class': 'form-input', 'icon': 'image'})
        }