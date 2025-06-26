from utils.getIds import getIds
from utils.getAllData import getAllData

def main():
  course_year = 1
  liter = 1
  period = '20240901-20240902'
  ids = getIds(course_year,liter)
  print(ids)
  getAllData(ids, period,course_year,liter)
  print('Данные сохранены!')
  
		
if __name__ == "__main__":
    main()