import requests 
from config import API_URL, API_PARAMS

def get_data(ej_id, period):
    id =str(ej_id).replace(" ", "")
    urlGetAssessments = f"{API_URL}/getassessments?{API_PARAMS}&student={id}&days={period}"
    urlGetSchedule = f"{API_URL}/getschedule?{API_PARAMS}&student={id}&days={period}&rings=no"

    responseSchedule = requests.get(urlGetSchedule)
    responseAssessments = requests.get(urlGetAssessments)
    dataSchedule = None
    dataAssessments = None
    if responseSchedule: dataSchedule = responseSchedule.json()
    if responseAssessments: dataAssessments = responseAssessments.json()
    


    return dataSchedule, dataAssessments