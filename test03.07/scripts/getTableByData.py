from scripts.getData import get_data
from utils.getTeacher import get_teacher
import pandas as pd

def get_table(ej_id, period):
	dataSchedule, dataAssessments = get_data(ej_id, period)
	student_assessment = None
	student_schedule = None
	rows = []

	if dataAssessments.get('response',{}).get('result',{}).get('students') is not None:
		student_assessment = dataAssessments.get('response',{}).get('result',{}).get('students').values()
	if dataSchedule.get('response',{}).get('result',{}).get('students').values() is not None:
		student_schedule =dataSchedule.get('response',{}).get('result',{}).get('students').values()
	
	if student_assessment and student_schedule:
		for student in student_assessment:
			id = int(student['name'])
			title = student['title']
			if student.get('days',None) is None: continue
			for days in student['days'].values():
				day = days['name']
				if days.get('items', None) is None: continue
				for item in days['items'].values():
					course_name = item['name']
					teacher = get_teacher(course_name, student_schedule, day)
					for assessment in item.get('assessments', []):
						value_raw = assessment.get('value', '')
						try:
							value = int(value_raw)
						except (ValueError, TypeError):
							value = 0
						control_str = str(assessment.get('control_type_short', ''))
						digits_only = ''.join(filter(str.isdigit, control_str))	
						max_value = int(''.join(filter(str.isdigit, digits_only))) if 	digits_only else 0
						lesson_comment = assessment.get('lesson_comment', '')
						comment = assessment.get('comment', '')
						rows.append({
							'date':day,
							'id':id,
							'title':title,
							# 'course_year':course_year,
							# 'liter':liter,
							# 'site':site,
							# 'trimester':trimester,
							# 'school_year':school_year,
							'course_name': course_name,
							'teacher':teacher,
  	          'score': value,
							'weight':max_value,
  	          'lesson_comment': lesson_comment,
							'score_comment':comment
					})

	df = pd.DataFrame(rows)
	print(df)

