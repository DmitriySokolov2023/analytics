import pandas as pd

def get_classes():
	unique_data = []
	df = pd.read_excel("tables/az_ids.xlsx")  # или pd.read_csv("students.csv")
	result = df[["course_year", "liter"]].values.tolist()
	for sublist in result:
		if sublist not in unique_data:
			unique_data.append(sublist)
	return unique_data