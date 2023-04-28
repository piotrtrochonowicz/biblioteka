from django.shortcuts import render, redirect
from .models import Book, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm, AddBookForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


# Create your views here.


def home_screen_view(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    liked_by_critics = Book.objects.filter(liked_by_critics=True)
    best_sellers = Book.objects.filter(best_sellers=True)
    return render(request, 'home.html', {'recommended_books': recommended_books,
                                         'liked_by_critics': liked_by_critics, 'best_sellers': best_sellers})


def all_books_view(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def category_details_view(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'category_details.html', {'category': category})


@login_required(login_url='login')
def book_details_view(request, slug):
    book = Book.objects.get(slug=slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(
        category__name__startswith=book_category)
    return render(request, 'book_details.html', {'book': book, 'similar_books': similar_books})


def search_book_view(request):
    searched_book = Book.objects.filter(
        title__icontains=request.POST.get('book_name',))

    return render(request, 'search_book.html', {'searched_book': searched_book})


def signup_view(request):
    signup_form = RegisterUserForm()
    if request.method == 'POST':
        signup_form = RegisterUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.info(
                request, "Gratulacje. Udało się utworzyć konto! (•‿•)")
            return redirect('login')
    return render(request, 'signup.html', {'signup_form': signup_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Nieprawidłowe dane logowania!")

    return render(request, 'login.html', {})


def logout_user_view(request):
    logout(request)
    return redirect('home')


def add_book_view(request):
    submitted = False
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_book?submitted=TRUE')

    else:
        form = AddBookForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_book.html', {'form': form, 'submitted': submitted})


def about_view(request):
    return render(request, 'about.html', {})


def update_user_profile(request):
    if request.user.is_authenticated:
        logged_user = User.objects.get(id=request.user.id)
        signup_form = RegisterUserForm(
            request.POST or None, instance=logged_user)
        if signup_form.is_valid():
            signup_form.save()
            login(request, logged_user)
            return redirect('home')
    return render(request, 'update_user_profile.html', {'signup_form': signup_form})
