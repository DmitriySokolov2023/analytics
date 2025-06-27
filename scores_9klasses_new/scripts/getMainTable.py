from utils.getCourse import get_course
from utils.getTeacher import get_teacher
from utils.getTrimester import get_trimester

def get_main_table(dataSchedule, dataAssessments, rows, id):
	students = dataAssessments['response']['result']['students']
	students_initial = dataSchedule['response']['result']['students']
	student_check = dataAssessments['response']['result']['students'].get(id)
	course_year, liter, site, school_year = get_course(id)

	if 'days' not in student_check:
		for student_initial in students_initial.values():
			title = student_initial['title']
			for day in student_initial['days'].values():
				day_name = day['name']
				trimester = get_trimester(day_name)
				value = -1
				max_value = -1
				if not day.get('items'):continue
				for lesson in day['items'].values():
					subject_name = lesson['name']
					teacher = get_teacher(dataSchedule, subject_name, day_name,id)
					lesson_comment = ''
					comment = ''
					rows.append({
							'date':day_name,
							'Ej_ID':id,
  	          'title': title,
							'course_year':course_year,
							'liter':liter,
							'site':site,
							'trimester':trimester,
							'school_year':school_year,
							'course_name': subject_name,
							'teacher':teacher,
  	          'score': value,
							'weight':max_value,
  	          'lesson_comment': lesson_comment,
							'score_comment':comment})
	else:
		for student in students.values():
			print(student)
			title = student['title']
			for day in student['days'].values():
				
				day_name = day['name']
				trimester = get_trimester(day_name)
				for lesson in day['items'].values():
					subject_name = lesson['name']
					teacher = get_teacher(dataSchedule, subject_name, day_name,id)
					for assessment in lesson.get('assessments', []):
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
							'date':day_name,
							'Ej_ID':id,
  	          'title': title,
							'course_year':course_year,
							'liter':liter,
							'site':site,
							'trimester':trimester,
							'school_year':school_year,
							'course_name': subject_name,
							'teacher':teacher,
  	          'score': value,
							'weight':max_value,
  	          'lesson_comment': lesson_comment,
							'score_comment':comment})
					
	return rows	