import json
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