import requests 

def getSchedule(ej_id, period):
    id = ej_id.replace(" ", "")
    urlGetAssessments = f"https://edu.gounn.ru/api/getassessments?devkey=bc4e58bf8c4f389f4a25256da1468baf&login=shkola800&password=bdf0389402d33a7f7ab6924e10fe401d&vendor=nnov0985&token=d3d583dbc7c250ecb8a82ba4a086e91af1e3f3fdc9742121ccab703af8fc1___152565&student={id}&days={period}"
    urlGetSchedule = f"https://edu.gounn.ru/api/getschedule?devkey=bc4e58bf8c4f389f4a25256da1468baf&login=shkola800&password=bdf0389402d33a7f7ab6924e10fe401d&vendor=nnov0985&token=d3d583dbc7c250ecb8a82ba4a086e91af1e3f3fdc9742121ccab703af8fc1___152565&student={id}&days={period}&rings=no"

    responseSchedule = requests.get(urlGetSchedule)
    responseAssessments = requests.get(urlGetAssessments)

    dataSchedule = responseSchedule.json()
    dataAssessments = responseAssessments.json()

    return dataSchedule, dataAssessments