from django.urls import path

from covidData.views import covidResearch, covidDataScraper, home, commodityData, commodityDataScraper, currencyData, currencyDataScraper, insiderTradingData, insiderTradingData

urlpatterns = [
    path('', home, name='home'),
    path('covidResearch/', covidResearch, name='covidResearch'),
    path('covidDataScraper/', covidDataScraper, name='covidDataScraper'),
    path('currencyData/', currencyData, name='currencyData'),
    path('currencyDataScraper/', currencyDataScraper, name='currencyDataScraper'),
    path('commodityData/', commodityData, name='commodityData'),
    path('commodityDataScraper/', commodityDataScraper, name='commodityDataScraper'),
    path('insiderTradingData/', insiderTradingData, name='insiderTradingData'),
    path('insiderTradingData/', insiderTradingData, name='insiderTradingData'),
]