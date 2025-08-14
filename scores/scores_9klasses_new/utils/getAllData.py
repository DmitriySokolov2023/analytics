from scripts.getMainTable import get_main_table
from utils.getExcel import get_excel
from scripts.getData import getData
from pprint import pprint

def getAllData(ids, period,course_year,liter):
	all_data = []

	for id in ids:
		dataSchedule, dataAssessments = getData(id,period)
		if (not dataSchedule or'result' not in dataSchedule['response'] or not dataSchedule['response']['result']):continue
		if (not dataAssessments or'result' not in dataAssessments['response'] or not dataAssessments['response']['result'].get('students')): continue 
		all_data = get_main_table(dataSchedule, dataAssessments, all_data, id)
	get_excel(all_data,course_year,liter)