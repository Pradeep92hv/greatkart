
from .models import Category

def menu_links(request):
    all_links=Category.objects.all()
    return dict(links=all_links)