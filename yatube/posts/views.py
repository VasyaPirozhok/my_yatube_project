from django.http import HttpResponse


def index(request):
    return HttpResponse('Это главная страница')

def group_posts(request, slug):
    return HttpResponse('Список постов')


