import requests


parameters = {"fields": "BriefTitle,BriefSummary,DetailedDescription,StudyType,Phase,EnrollmentCount,StartDate,PrimaryCompletionDate,ArmGroupInterventionName,PrimaryOutcomeMeasure,SecondaryOutcomeMeasure", 
            "fmt": "JSON",
            "expr": "covid"}

response = requests.get("https://clinicaltrials.gov/api/query/study_fields?", params=parameters)

data = response.json()
jsonResult = data["StudyFieldsResponse"]
topStudies = jsonResult["StudyFields"]

for i in range(len(topStudies)):
    individualStudy = topStudies[i]
    temp = str(individualStudy["BriefTitle"])[2:-2]
    print(temp)