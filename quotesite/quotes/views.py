from django.shortcuts import render
from .utils import get_mongodb
from django.core.paginator import Paginator
from bson.objectid import ObjectId
from .models import Quote, Tag, Author


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    print(list(quotes))
    return render(request, 'quotes/index.html', context={'quotes':quotes_on_page})

def author_about(request, author_id):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(author_id)})  # Використання ObjectId(author_id)
    return render(request, 'quotes/author.html', context={'author': author})

def tag_page(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    quotes_with_tag = Quote.objects.filter(tags=tag)
    return render(request, 'quotes/tag.html', {'quotes_with_tag': quotes_with_tag, 'tag': tag})


def author_for_tag(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_for_tag.html', context={'author': author})
