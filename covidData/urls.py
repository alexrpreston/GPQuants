from django.urls import path

from covidData.views import index, scrape

urlpatterns = [
    path('', index, name='index'),
    path('scrape/', scrape, name='scrape'),
]