import pandas as pd
def get_course(ej_id):
	df = pd.read_excel("tables/az_ids.xlsx")
	ej_id_clean = str(ej_id).replace(' ', '')
	result = df[df['ej_id'].astype(str).str.replace(' ', '') == ej_id_clean]
	if not result.empty:
		course_year = result.iloc[0]['course_year']
		liter = result.iloc[0]['liter']
		return course_year, liter, 'АЗ', '2024'
	else:return None
	