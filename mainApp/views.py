from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html',
                  {"values":["если шо, зовните сюда", '000-00-00-0']})
