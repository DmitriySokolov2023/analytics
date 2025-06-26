import pandas as pd

def get_excel(table, course_year, liter):
	df = pd.DataFrame(table)
	df.to_excel(f"data/{course_year}-{liter}_assessments_table.xlsx", index=False)
	return df