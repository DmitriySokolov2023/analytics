from scripts.getTableByData import get_table
from services.db import push_many_to_db
from utils.getClasses import get_classes





def main():
   classes = get_classes()
   period = '20240901-20250531'
   for cl in classes[:2]:
     id = cl[0]
     course_year = cl[1]
     liter = cl[2]
     rows = get_table(id, period, course_year, liter, 'АЗ', '2024')
     push_many_to_db('test_sokolov', rows )
     print(f'Информация по ученику {id} выгружена!')



if __name__ == "__main__":
    main()