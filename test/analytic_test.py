import requests
import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint

urlGetAssessments = "https://edu.gounn.ru/api/getassessments?devkey=bc4e58bf8c4f389f4a25256da1468baf&login=shkola800&password=bdf0389402d33a7f7ab6924e10fe401d&vendor=nnov0985&token=d3d583dbc7c250ecb8a82ba4a086e91af1e3f3fdc9742121ccab703af8fc1___152565&student=1171&days=20250501-20250507"
urlGetSchedule = "https://edu.gounn.ru/api/getschedule?devkey=bc4e58bf8c4f389f4a25256da1468baf&login=shkola800&password=bdf0389402d33a7f7ab6924e10fe401d&vendor=nnov0985&token=d3d583dbc7c250ecb8a82ba4a086e91af1e3f3fdc9742121ccab703af8fc1___152565&student=1171&days=20250501-20250507&rings=no"


responseSchedule = requests.get(urlGetSchedule)
dataSchedule = responseSchedule.json()

responseAssessments = requests.get(urlGetAssessments)
dataAssessments = responseAssessments.json()

print(dataSchedule)
def get_teacher(dataSchedule, subject_name, day):
	students = dataSchedule['response']['result']['students']
	for student in students.values():
		for teacher in student['days'][day]['items']




def get_assessments(data):
	rows = []
	students = data['response']['result']['students']

	for student in students.values():
		title = student['title']

		for day in student['days'].values():
			day_name = day['name']
			for lesson in day['items'].values():
				subject_name = lesson['name']
				teacher = get_teacher(dataSchedule, subject_name, day_name)
				for assessment in lesson.get('assessments', []):
					value = assessment.get('value',[])
					max_value =int(''.join(filter(str.isdigit, assessment.get('control_type_short', [])))) 
					lesson_comment = assessment.get('lesson_comment', '')
					comment = assessment.get('comment', '')
					rows.append({
						'date':day_name,
                        'title': title,
												'teacher':'учитель',
                        'subject': subject_name,
                        'value': value,
												'max_value':max_value,
                        'lesson_comment': lesson_comment,
												'comment':comment
                    })
	return rows

def in_excel(data):
	table = get_assessments(data)
	df = pd.DataFrame(table)
	df.to_csv("assessments_table.csv", index=False, encoding="utf-8-sig")



in_excel(dataAssessments)















# df = pd.DataFrame(data)

# df.to_csv("output.csv", index=False)


# df_read = pd.read_csv("output.csv")
# engine = create_engine("postgresql://sokolov:SySHjAoLXO3SxLZa0WNiTRQqtwhQxz2W@dpg-d13h9v3e5dus73eoofug-a.frankfurt-postgres.render.com/analytics_ycdp")

# df_read.to_sql("my_table", engine, if_exists="replace", index=False)