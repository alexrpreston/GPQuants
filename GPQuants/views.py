from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from newsapi import NewsApiClient
from GPQuants.models import covidHeadlines, covidClinicalTrials, covidTreatmentTypes
from .trialCSVData import getTreatmentTypes
import requests


def covidDataScraper(response):
    covidHeadlines.objects.all().delete()
    covidClinicalTrials.objects.all().delete()
    covidTreatmentTypes.objects.all().delete()
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
        new_headline.publishedData = f['publishedAt']
        new_headline.save()

    # ############################################################################

    parameters = {"fields": "BriefTitle,BriefSummary,DetailedDescription,StudyType,Phase,EnrollmentCount,StartDate,PrimaryCompletionDate,CompletionDate,ArmGroupInterventionName,PrimaryOutcomeMeasure,SecondaryOutcomeMeasure,InterventionType", 
            "fmt": "JSON",
            "expr": "(covid-19 OR coronavirus OR sars-cov-2) AND interventional NOT (observational AND observational)"}

    response = requests.get("https://clinicaltrials.gov/api/query/study_fields?", params=parameters)

    data = response.json()
    jsonResult = data["StudyFieldsResponse"]
    topStudies = jsonResult["StudyFields"]

    for i in range(len(topStudies)):
        individualStudy = topStudies[i]
        new_trial = covidClinicalTrials()
        new_trial.title = str(individualStudy["BriefTitle"])[2:-2]
        new_trial.briefSummary = str(individualStudy["BriefSummary"])[2:-2]
        new_trial.detailedDesc = str(individualStudy["DetailedDescription"])[2:-2]
        new_trial.studyType = str(individualStudy["StudyType"])[2:-2]
        new_trial.firstintervention = str(individualStudy["InterventionType"])[2:-2]
        new_trial.Phase = str(individualStudy["Phase"])[2:-2]
        new_trial.enrollment = str(individualStudy["EnrollmentCount"])[2:-2]
        new_trial.studyCompletionDate = str(individualStudy["CompletionDate"])[2:-2]
        new_trial.startDate = str(individualStudy["StartDate"])[2:-2]
        new_trial.primaryCompletionDate = str(individualStudy["PrimaryCompletionDate"])[2:-2]
        new_trial.armfirstintervention = str(individualStudy["ArmGroupInterventionName"])[2:-2]
        new_trial.primaryOutcomeMes = str(individualStudy["PrimaryOutcomeMeasure"])[2:-2]
        new_trial.secondaryOutcomeMes = str(individualStudy["SecondaryOutcomeMeasure"])[2:-2]
        new_trial.save()


    newTreatmentList = covidTreatmentTypes()
    treatments = getTreatmentTypes()
    for treatment in treatments:
        newTreatmentList.treatmentTypes.append(treatment[0])
        newTreatmentList.treatmentTypeFreq.append(int(treatment[1]/2))
    newTreatmentList.save()
    
    return redirect("../covidResearch")

def insiderTradingDataScraper(request):

    return redirect("../insiderTradingData")

def currencyDataScraper(request):
    
    return redirect("../currencyData")

def commodityDataScraper(request):
    
    return redirect("../commodityData")


def covidResearch(request):
    covidHeadlinesFull = covidHeadlines.objects.all()[8:]
    covidTrialsFull = covidClinicalTrials.objects.all()
    treatmentTypes = covidTreatmentTypes.objects.first()
    context = {
        "covidtrials": covidTrialsFull,
        "covidHeadline": covidHeadlinesFull,
        "covidTreatments": treatmentTypes,
    }
    return render(request, "GPQuants/covidData.html", context)

def insiderTradingData(request):
    context = {
        
    }
    return render(request, "GPQuants/insiderTradingData.html", context)


def currencyData(request):
    context = {
        
    }
    return render(request, "GPQuants/currencyData.html", context)

def commodityData(request):
    context = {

    }
    return render(request, "GPQuants/commodityData.html", context)


def home(request):
    return render(request, "GPQuants/home.html")