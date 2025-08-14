from datetime import datetime

trimesters = {
    '1': ('2024-09-01', '2024-11-23'),
    '2': ('2024-11-24', '2025-02-23'),
    '3': ('2025-02-24', '2025-05-31')
}


def get_trimester(date_str):
  date = datetime.strptime(date_str, "%Y%m%d").date()
  for trimester, (start, end) in trimesters.items():
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()
    if start_date <= date <= end_date:
      return int(trimester) 
    else: continue
