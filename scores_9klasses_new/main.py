from scripts.getData import getData
import pandas as pd
from scripts.getMainTable import get_main_table
from utils.getExcel import get_excel

def main(period):
  df = pd.read_excel("tables/ids_9klass.xlsx")
  ids = df['ej_id'].astype(str).tolist()
  all_data = []
  for id in ids:
    dataSchedule, dataAssessments = getData(id,period)
    if (not dataSchedule or'result' not in dataSchedule['response'] or not dataSchedule['response']['result']):continue
    if (not dataAssessments or'result' not in dataAssessments['response'] or not dataAssessments['response']['result'].get('students')): continue
    all_data = get_main_table(dataSchedule, dataAssessments, all_data, id)
    get_excel(all_data)
		
if __name__ == "__main__":
    main('20250501-20250530')