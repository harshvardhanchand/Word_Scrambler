# scrambler/urls.py
from django.urls import path
from . import views

app_name = 'word_scrambler_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.index, name='results'),
]


