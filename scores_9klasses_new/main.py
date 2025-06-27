from utils.getIds import getIds
from utils.getAllData import getAllData
from utils.getClasses import get_classes
def main():
  classes = get_classes()
  period = '20240901-20250531'
  for cl in classes:
     course_year = cl[0]
     liter = cl[1]
     ids = getIds(course_year,liter)
     print(course_year, liter,ids)
     getAllData(ids, period,course_year,liter)
     print(f'Данные сохранены ({course_year}-{liter})!')
  
		
if __name__ == "__main__":
    main()