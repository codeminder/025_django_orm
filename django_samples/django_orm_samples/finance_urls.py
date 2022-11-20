from .views import *
from django.urls import path
from django.conf.urls.static import static
from django_samples import settings

urlpatterns = [
    path('', index, name="home"),
    path('journal/full/', journal_full, name="journal_full"),
    path('journal/<str:type_doc>/', journal, name="journal_doc"),
    path('journal/', journal_full),
    path('about/', about, name="about"),
    path('login/', login, name="login"),
    path('journal/<str:type_doc>/<int:doc_id>/', view_doc, name="view_doc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)