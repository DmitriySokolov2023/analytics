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