from django import forms
from .models import SearchBook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Book


class SearchBookForm(forms.ModelForm):
    book_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Szukaj'
    }))

    class Meta:
        model = SearchBook
        fields = ['book_name']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'Podaj nazwę użytkownika'
    }))

    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-input', 'placeholder': 'Podaj adres e-mail'
    }))

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-input', 'placeholder': 'Podaj hasło'
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-input', 'placeholder': 'Potwierdź hasło'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description',
                  'category', 'cover_image', 'pdf')

        labels = {
            'title': '',
            'author': '',
            'description': '',
            'category': '',
            'cover_image': 'Okładka:',
            'pdf': 'PDF:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Tytuł'}),
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Autor'}),
            'description': forms.Textarea(attrs={'class': 'form-input-desc', 'placeholder': 'Opis'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-input-category', 'placeholder': 'Kategoria'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control-cover_image', 'placeholder': 'Zdjęcie Okładki'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control-pdf', 'placeholder': 'Plik PDF'}),
        }
