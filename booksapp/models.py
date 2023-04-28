from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField('Categories', max_length=60)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    slug = models.SlugField(max_length=100, unique=True)
    # blank=True, null=True, ponieważ gdy w bazie danych nie będzie zdjęcia książki nie będzie błędów
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    best_sellers = models.BooleanField(default=False)
    liked_by_critics = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class SearchBook(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
