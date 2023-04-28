from .models import Category
from .forms import SearchBookForm


def category_links(request):
    category = Category.objects.all()
    return {'categories': category}


def search_book(request):
    search_form = SearchBookForm
    if request.method == 'POST':
        search_form = SearchBookForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return {'search_form': search_form}
