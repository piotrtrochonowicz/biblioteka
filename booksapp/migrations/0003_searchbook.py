# Generated by Django 4.1.4 on 2023-02-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0002_rename_biography_books_book_best_sellers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
    ]