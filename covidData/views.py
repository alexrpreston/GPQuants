from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from newsapi import NewsApiClient
from covidData.models import covidHeadlines


def scrape(response):
    covidHeadlines.objects.all().delete()


    newsapi = NewsApiClient(api_key = "7890f99f817b40a0a587325193ca0933")
    top = newsapi.get_everything(q ='(covid OR coronavirus) AND (treatment OR vaccine)')
    # q ='(covid OR coronavirus) AND (treatment OR vaccine)'
    tcl = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(tcl)):
        f = tcl[i]
        new_headline = covidHeadlines()
        new_headline.title = f['title']
        sources = f['source']
        new_headline.source = sources['name']
        print(new_headline.title)
        new_headline.url = f['url']
        new_headline.desc = f['description']
        new_headline.save()

    return redirect("../")

    

def index(request):
    covidHeadlinesFull = covidHeadlines.objects.all()[8:]

    context = {
        "covidHeadline": covidHeadlinesFull,
    }
    return render(request, "covidData/home.html", context)
