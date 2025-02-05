from django.urls import path

from GPQuants.views import covidResearch, covidDataScraper, home, commodityData, commodityDataScraper, currencyData, currencyDataScraper, insiderTradingData, insiderTradingData, homeWithData

urlpatterns = [
    path('', homeWithData, name='homeWithData'),
    path('covidResearch/', covidResearch, name='covidResearch'),
    path('covidDataScraper/', covidDataScraper, name='covidDataScraper'),
    path('currencyData/', currencyData, name='currencyData'),
    path('currencyDataScraper/', currencyDataScraper, name='currencyDataScraper'),
    path('commodityData/', commodityData, name='commodityData'),
    path('commodityDataScraper/', commodityDataScraper, name='commodityDataScraper'),
    path('insiderTradingData/', insiderTradingData, name='insiderTradingData'),
    path('insiderTradingData/', insiderTradingData, name='insiderTradingData'),

]