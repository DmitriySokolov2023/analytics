def get_teacher(course_name, student_schedule, date):
	for student in student_schedule:
		if student.get('days') is None: return None
		for day in student['days'].values():
			if day['name'] != date:continue
			for item in day['items'].values():
				if item['name'] == course_name: return item['teacher']


