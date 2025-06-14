import requests
import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint
import json
from services.getSchedule import getSchedule
from services.dbPush import push_in_db

def get_teacher(dataSchedule, subject_name, date,id):
	id_stud = id.replace(" ","")
	days = dataSchedule['response']['result']['students'][id_stud]['days']
	day = days.get(date)

	for lesson in day.get('items', {}).values():
		if lesson.get('name') == subject_name:
			return lesson.get('teacher')
	for lesson in day.get('items_extday', []):
		if lesson.get('name') == subject_name:
			return lesson.get('teacher')
	
def get_course(ej_id):
	data = []
	with open("tables/scores.json", "r", encoding="utf-8") as f:
		data = json.load(f)
	cleaned_id = ej_id.replace(" ", "")
	for  record in data:
		record_id = str(record.get("Ej ID", "")).replace(" ", "")
		if record_id == cleaned_id:
			course_name = record.get("Course Year")
			liter = record.get('Liter')
			site = record.get('Site')
			school_year = record.get('School Year')
			return course_name, liter, site, school_year


		
	return None, None

def get_assessments(dataSchedule, dataAssessments, rows, id):
	students = dataAssessments['response']['result']['students']
	course_year, liter, site, school_year = get_course(id)
	for student in students.values():
		title = student['title']

		for day in student['days'].values():
			day_name = day['name']
			for lesson in day['items'].values():
				subject_name = lesson['name']
				teacher = get_teacher(dataSchedule, subject_name, day_name,id)
				for assessment in lesson.get('assessments', []):
					value_raw = assessment.get('value', '')
					try:
						value = int(value_raw)
					except (ValueError, TypeError):
						value = value_raw
					control_str = str(assessment.get('control_type_short', ''))
					max_value = int(''.join(filter(str.isdigit, control_str))) if control_str else 0
					lesson_comment = assessment.get('lesson_comment', '')
					comment = assessment.get('comment', '')
					
					rows.append({
						'date':day_name,
						'Ej_ID':id,
                        'title': title,
						'course_year':course_year,
						'liter':liter,
						'site':site,
						'school_year':school_year,
						'course_name': subject_name,
						'teacher':teacher,
                        'score': value,
						'weight':max_value,
                        'lesson_comment': lesson_comment,
						'score_comment':comment
                    })
	return rows

def in_excel(table):
	df = pd.DataFrame(table)
	
	df.to_excel("tables/assessments_table.xlsx", index=False)
	# push_in_db()

def main(period):
	df = pd.read_excel("tables/ids.xlsx")
	ids = df['ej_id'].astype(str).tolist()
	all_data = []
	for id in ids:
		dataSchedule, dataAssessments = getSchedule(id,period)
		if (not dataSchedule or'result' not in dataSchedule['response'] or not dataSchedule['response']['result']):continue
		if (not dataAssessments or'result' not in dataAssessments['response'] or not dataAssessments['response']['result'].get('students')): continue

		all_data = get_assessments(dataSchedule, dataAssessments, all_data, id)
	in_excel(all_data)
	



main('20250501-20250507')














# df = pd.DataFrame(data)

# df.to_csv("output.csv", index=False)


# df_read = pd.read_csv("output.csv")
# engine = create_engine("postgresql://sokolov:SySHjAoLXO3SxLZa0WNiTRQqtwhQxz2W@dpg-d13h9v3e5dus73eoofug-a.frankfurt-postgres.render.com/analytics_ycdp")

# df_read.to_sql("my_table", engine, if_exists="replace", index=False)