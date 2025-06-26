from utils.getCourse import get_course
from utils.getTeacher import get_teacher

def get_main_table(dataSchedule, dataAssessments, rows, id):
	students = dataAssessments['response']['result']['students']
	students_initial = dataSchedule['response']['result']['students']
	print(students_initial)
	course_year, liter, site, school_year = get_course(id)
	if 'days' not in students:
		for student_initial in students_initial.values():
			title = student_initial['title']
			for day in student_initial['days'].values():
				day_name = day['name']
				for lesson in day['items'].values():
					subject_name = lesson['name']
					teacher = get_teacher(dataSchedule, subject_name, day_name,id)
					value = -1
					max_value = -1
					lesson_comment = ''
					comment = ''
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
							'score_comment':comment})
	else:
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
							value = None
						control_str = str(assessment.get('control_type_short', ''))
						digits_only = ''.join(filter(str.isdigit, control_str))	
						max_value = int(''.join(filter(str.isdigit, digits_only))) if 	digits_only else 0
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
							'score_comment':comment})
					
	return rows	