from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('all_books', views.all_books_view, name='all_books'),
    path('category/<str:slug>', views.category_details_view,
         name='category_details'),
    path('book/<str:slug>', views.book_details_view, name="book_details"),
    path('search', views.search_book_view, name="search_book"),
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_user_view, name="logout"),
    path('add_book', views.add_book_view, name="add_book"),
    path('about', views.about_view, name="about"),
    path('update_user_profile', views.update_user_profile,
         name="update_user_profile"),
]
