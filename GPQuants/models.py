from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class covidHeadlines(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)
    publishedData = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class covidClinicalTrials(models.Model):
    title = models.CharField(max_length=200)
    briefSummary = models.TextField(null=True, blank=True)
    detailedDesc = models.TextField(null=True, blank=True)
    studyType = models.CharField(max_length=200)
    studyPhase = models.CharField(max_length=200)
    firstintervention = models.CharField(max_length=200)
    secondintervention = models.CharField(max_length=200)
    enrollment = models.CharField(max_length=200)
    startDate = models.CharField(max_length=200)
    primaryCompletionDate = models.CharField(max_length=200)
    studyCompletionDate = models.CharField(max_length=200)
    armfirstintervention = models.CharField(max_length=200)
    armSecondintervention = models.CharField(max_length=200)
    primaryOutcomeMes = models.TextField(null=True, blank=True)
    secondaryOutcomeMes = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.title

class covidTreatmentTypes(models.Model):
    treatmentTypes = ArrayField(models.TextField(blank=True, null=True, default=""), default=list)
    treatmentTypeFreq = ArrayField(models.TextField(blank=True, null=True, default=""), default=list)

class currencies(models.Model):
    firstCurrencyChoice = models.TextField()
    secondCurrencyChoice = models.TextField()
    