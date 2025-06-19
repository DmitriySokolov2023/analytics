import pandas as pd

def get_excel(table):
	df = pd.DataFrame(table)
	df.to_excel("data/assessments_table.xlsx", index=False)
	return df