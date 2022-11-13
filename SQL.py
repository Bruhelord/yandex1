# Импорт библиотеки
import random
import sqlite3

COMMAND_CHOOSE_TASKS = """SELECT task, answer FROM tasks"""
COMMAND_CHANGE_HISTORY = """INSERT INTO history_of_tasks
    (task, date, your_answer, right_answer)
    VALUES
    (?, ?, ?, ?);"""
COMMAND_UPDATE_HISTORY = "UPDATE history_of_tasks SET task = ?, date = ?, your_answer = ?, right_answer = ? WHERE date = ?"
COMMAND_DELETE_ALL = """DELETE from history_of_tasks"""
COMMAND_SELECT = "SELECT id, task, date, your_answer, right_answer FROM history_of_tasks"
COMMAND_DELETE_SELECTED = """DELETE from history_of_tasks where id = ?"""


def choose_tasks(n):
    '''функция выбора задач'''
    sqlite_connection = sqlite3.connect("tasks.db")
    cursor = sqlite_connection.cursor()
    tasks = random.sample(cursor.execute(COMMAND_CHOOSE_TASKS).fetchall(), n)
    sqlite_connection.close()
    return tasks


def change_history(task, date, your_answer, right_answer):
    '''функция добавления данных в историю'''
    sqlite_connection = sqlite3.connect("history_of_tasks.db")
    cursor = sqlite_connection.cursor()

    data = (str(task), str(date), str(your_answer), str(right_answer))
    cursor.execute(COMMAND_CHANGE_HISTORY, data)
    sqlite_connection.commit()
    sqlite_connection.close()



def update_last(task, date, your_answer, right_answer, new_date):
    '''функция для обновления сохраненного ответа'''
    sqlite_connection = sqlite3.connect("history_of_tasks.db")
    cursor = sqlite_connection.cursor()
    cursor.execute(COMMAND_UPDATE_HISTORY, (task, new_date, your_answer, right_answer, date))
    sqlite_connection.commit()
    sqlite_connection.close()


def show_all_history():
    sqlite_connection = sqlite3.connect("history_of_tasks.db")
    cursor = sqlite_connection.cursor()
    data = cursor.execute(COMMAND_SELECT).fetchall()
    sqlite_connection.close()
    return data


def delete_all():
    sqlite_connection = sqlite3.connect("history_of_tasks.db")
    cursor = sqlite_connection.cursor()
    cursor.execute(COMMAND_DELETE_ALL)
    sqlite_connection.commit()
    sqlite_connection.close()


def delete_selected_row(task_id):
    '''функция удаляет выбранную строку из базы данных'''
    sqlite_connection = sqlite3.connect("history_of_tasks.db")
    cursor = sqlite_connection.cursor()
    cursor.execute(COMMAND_DELETE_SELECTED.replace('?', str(task_id)))
    sqlite_connection.commit()
    sqlite_connection.close()
