from datetime import datetime, date, time
from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    print(get_employees())
    print(calculate_salary())
    print(datetime.now().strftime("%H:%M:%S"),date.today())
