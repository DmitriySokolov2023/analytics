import pandas as pd

def getIds(course_year, liter):
	df = pd.read_excel("tables/az_ids.xlsx")
	filtered_data = df[(df['course_year'] == course_year) & (df['liter'] == liter)]
	ids = filtered_data['ej_id'].astype(str).tolist()
	return ids

