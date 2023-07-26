from django.views.defaults import page_not_found
from django.shortcuts import render
from django.http import HttpResponse


# обработка единственной страницы сайта
def index(request):
    return render(request, 'main/nasa.html')


# обработка отсутствующей страницы
def page_not_found_view(request, exception):
    response = page_not_found(request, exception,
                              template_name='main/404.html')
    response.status_code = 404
    return response
