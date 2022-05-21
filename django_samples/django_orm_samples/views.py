
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *

# Create your views here.

menu = [{"title": "Статистика", "url_name": "home"}, 
        {"title": "Журнал", "url_name": "journal_full"}, 
        {"title": "О сайте", "url_name": "about"}, 
        {"title": "Войти", "url_name": "login"}]

def index(request):
    # return HttpResponse("Главная страница приложения")
    return render(request, "django_orm_samples/index.html", {"title": "Главная страница", "menu": menu})

def login(request):
    return HttpResponse("Страница логин")

def about(request):
    # return HttpResponse("Главная страница приложения")
    return render(request, "django_orm_samples/about.html", {"title": "О сайте"})

def journal_full(request):
    return HttpResponse("<h2>Страница полного журнала</h2>")

def journal(request, type_doc):
    
    if type_doc.lower() == 'Profit'.lower():
        # docs = Profit.objects.all()
        return render(request, "django_orm_samples/journal.html", context=get_journal_data(Profit))
    elif type_doc.lower() == 'Cost'.lower():
        # docs = Cost.objects.all()
        return render(request, "django_orm_samples/journal.html", context=get_journal_data(Cost))
    elif type_doc.lower() == 'Transfer'.lower():
        # docs = Transfer.objects.all()
        return render(request, "django_orm_samples/journal.html", context=get_journal_data(Transfer))
    elif type_doc.lower() == 'Inventory'.lower():
        # docs = Inventory.objects.all()
        return render(request, "django_orm_samples/journal.html", context=get_journal_data(Inventory))
    elif type_doc.lower() == 'CurrencyExchange'.lower():
        # docs = CurrencyExchange.objects.all()
        return render(request, "django_orm_samples/journal.html", context=get_journal_data(CurrencyExchange))
    else:
        raise Http404()
    
def get_journal_data(class_of_object):
    docs = class_of_object.objects.all()
    return  {"title": class_of_object._meta.verbose_name_plural, "docs": docs, "menu": menu}

def view_doc(request, type_doc, doc_id):
    return HttpResponse(f"Отображение документа {type_doc} {doc_id}")
    
    
