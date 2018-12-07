from django.shortcuts import render
from .models import Bookmark


def index(request):
    bookmarks = Bookmark.objects.order_by('-created_at')
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarks/index.html', context)
