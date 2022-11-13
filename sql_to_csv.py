import csv
import sqlite3
from SQL import COMMAND_SELECT


def import_to_csv():
    '''функция импорта истории.db в /csv'''
    try:
        with open('history_of_tasks.csv', 'w', newline='', encoding='utf-16') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['id', 'task', 'date', 'your_answer', 'right_answer'])
            sqlite_connection = sqlite3.connect("history_of_tasks.db")
            cursor = sqlite_connection.cursor()

            data = cursor.execute(COMMAND_SELECT).fetchall()
            for i in data:
                writer.writerow([str(i[0]).strip(), str(i[1]).strip(), str(i[2]).strip(), str(i[3]).strip(), str(i[4]).strip()])
            sqlite_connection.close()
    except PermissionError:
        pass



import_to_csv()