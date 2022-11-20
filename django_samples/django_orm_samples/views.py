
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

JOURNAL_CLASSES = [Profit, Cost, Transfer, Inventory, CurrencyExchange]

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
    # return HttpResponse("<h2>Страница полного журнала</h2>")
    return render(request, "django_orm_samples/journal.html", context=get_full_journal_context())

def journal(request, type_doc):
    
    return render(request, "django_orm_samples/journal.html", context=get_journal_context(get_class_for_typedoc(type_doc)))
    
    # if type_doc.lower() == 'Profit'.lower():
    #     # docs = Profit.objects.all()
    #     return render(request, "django_orm_samples/journal.html", context=get_journal_context(Profit))
    # elif type_doc.lower() == 'Cost'.lower():
    #     # docs = Cost.objects.all()
    #     return render(request, "django_orm_samples/journal.html", context=get_journal_context(Cost))
    # elif type_doc.lower() == 'Transfer'.lower():
    #     # docs = Transfer.objects.all()
    #     return render(request, "django_orm_samples/journal.html", context=get_journal_context(Transfer))
    # elif type_doc.lower() == 'Inventory'.lower():
    #     # docs = Inventory.objects.all()
    #     return render(request, "django_orm_samples/journal.html", context=get_journal_context(Inventory))
    # elif type_doc.lower() == 'CurrencyExchange'.lower():
    #     # docs = CurrencyExchange.objects.all()
    #     return render(request, "django_orm_samples/journal.html", context=get_journal_context(CurrencyExchange))
    # else:
    raise Http404()
    
def get_journal_context(class_of_object):
    docs = class_of_object.objects.all()
    return  {"title": class_of_object._meta.verbose_name_plural, "docs": docs, "menu": menu, 
             "types_of_docs": get_types_of_docs(), "type_doc": class_of_object._meta.model_name}
    
def get_full_journal_context():
    docs = Cost.objects.all()
    return  {"title": "Все документы", "docs": docs, "menu": menu, 
             "types_of_docs": get_types_of_docs(), "type_doc": None}

def view_doc(request, type_doc, doc_id):
    
    # return HttpResponse(f"Отображение документа {type_doc} {doc_id}")
    class_doc = get_class_for_typedoc(type_doc)
    doc = get_object_or_404(class_doc, pk=doc_id)

    context = {
        'doc': doc, 
        'menu': menu, 
        'title': str(doc), 
        'cat_selected': type_doc,
        }
    
    return render(request, "django_orm_samples/doc.html", context=context)

def  get_types_of_docs():
    
    type_doc = []
    
    for class_doc in JOURNAL_CLASSES:
        type_doc.append({"name": class_doc._meta.verbose_name_plural, "type_doc": class_doc._meta.model_name})
        
    return type_doc
    
def get_class_for_typedoc(type_doc):
     for class_doc in JOURNAL_CLASSES:
        if (type_doc.lower() ==  class_doc._meta.model_name):
            return class_doc    
