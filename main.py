import datetime
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWizardPage, QWizard, QWidget, QTableWidgetItem

from SQL import *
from TaskPageMain import UiTaskPageMain
from UiAmountOfTasks import UiAmountOfTasks
from UiHistoryOfTasks import UiHistoryOfTasks
from UiLastPage import UiLastPage
from UiStartPage import UiStartPage
from UiTaskPage import UiTaskPage
from sql_to_csv import import_to_csv

count_of_right_tasks = 0


class MainWidget(QMainWindow, UiStartPage):
    def __init__(self):
        super().__init__()
        self.ex2 = MyWidgetCount()
        self.setupUi(self)
        self.ex3 = HistoryPage()
        self.btn_make_variant.clicked.connect(self.make_variant)
        self.btn_open_history.clicked.connect(self.open_history)

    def make_variant(self):
        self.ex2.show()
        ex.hide()

    def open_history(self):
        self.ex3.show()
        ex.hide()


class MyWidgetCount(QMainWindow, UiAmountOfTasks):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start)
        self.count = None
        self.widget = None

    def start(self):
        self.count = self.spinBox_amount_of_tasks.value()
        self.widget = MyWidgetTaskMain(self.count)
        self.hide()
        self.widget.show()

    def closeEvent(self, event):
        ex.show()


class MyWidgetTaskMain(QWizard, UiTaskPageMain):
    def __init__(self, count):
        global count_of_right_tasks
        self.last_page = None
        super(MyWidgetTaskMain, self).__init__()
        self.count = count
        self.button(QWizard.WizardButton.FinishButton).clicked.connect(self.show_result)
        self.setupUi(self)
        self.tasks = choose_tasks(count)
        self.spisok = []
        for i in range(count):
            ex_task = MyWidgetTask(self.tasks[i])
            self.addPage(ex_task)
            self.spisok.append(ex_task)

    def show_result(self):
        global count_of_right_tasks
        for i in self.spisok:
            count_of_right_tasks += i.answer_true()
        self.last_page = MyWidgetLastPage(count_of_right_tasks, self.count)
        self.last_page.show()
        self.close()

    def closeEvent(self, event):
        self.close()


class MyWidgetTask(QWizardPage, UiTaskPage):
    def __init__(self, task):
        super().__init__()
        self.setupUi(self)
        self.task = task
        self.lbl_task.setText(task[0])
        self.answer_sent = False
        self.date = None
        self.lbl_task.setWordWrap(True)
        self.btn_send_a_reply.clicked.connect(self.send_answer)

    def send_answer(self):

        if not self.answer_sent:
            self.date = datetime.datetime.now(datetime.timezone.utc).astimezone()
            self.date = self.date.strftime("%Y-%m-%d %H:%M:%S")
            change_history(self.task[0], self.date, str(self.lineEditAnswer.text()), str(self.task[1]))
            self.answer_sent = True

        elif self.answer_sent:
            update_last(self.task[0],
                        self.date,
                        str(self.lineEditAnswer.text()),
                        str(self.task[1]),
                        datetime.datetime.now(datetime.timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S"))

    def closeEvent(self, event):
        self.close()

    def answer_true(self):
        if str(self.lineEditAnswer.text()) == str(self.task[1]):
            return 1
        else:
            return 0


class MyWidgetLastPage(QWidget, UiLastPage):
    def __init__(self, count_of_right_tasks, count_of_tasks):
        super(MyWidgetLastPage, self).__init__()
        self.setWindowTitle('Результат')
        self.setupUi(self)
        self.btn_OK.clicked.connect(self.ok)
        self.image = None
        self.lbl_result.setText(f'Вы решили {count_of_right_tasks}/{count_of_tasks} задач')
        if int(count_of_right_tasks) / int(count_of_tasks) >= 0.9:
            self.lbl_mark.setText('Оценка - 5')
            self.image = QPixmap('5.png')
            self.lbl_image.setPixmap(self.image)
        elif 0.66 <= (int(count_of_right_tasks) / int(count_of_tasks)) < 0.9:
            self.lbl_mark.setText('Оценка - 4')
            self.image = QPixmap('4.png')
            self.lbl_image.setPixmap(self.image)
        elif 0.5 < (int(count_of_right_tasks) / int(count_of_tasks)) < 0.66:
            self.lbl_mark.setText('Оценка - 3')
            self.image = QPixmap('3.png')
            self.lbl_image.setPixmap(self.image)
        else:
            self.lbl_mark.setText('Оценка - 2')
            self.image = QPixmap('2.png')
            self.lbl_image.setPixmap(self.image)

    def closeEvent(self, event):
        self.close()
        ex = MainWidget()
        ex.show()

    def ok(self):
        self.close()
        global ex_new
        ex_new = MainWidget()
        ex_new.show()


class HistoryPage(QWidget, UiHistoryOfTasks):
    def __init__(self):
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.create_table)
        self.timer.start()
        self.timer.stop()
        super(HistoryPage, self).__init__()
        self.setupUi(self)

        self.table_history.setColumnCount(5)
        self.table_history.setHorizontalHeaderLabels(['id', 'task', 'date', 'your_answer', 'right_answer'])

        self.btn_delete_all_history.clicked.connect(self.delete_all_history)
        self.btn_import_to_csv.clicked.connect(import_to_csv)
        self.btn_delete_choosen_history.clicked.connect(self.delete)
        self.data = None
        self.create_table()

    def closeEvent(self, event):
        self.close()
        ex.show()

    def delete_all_history(self):
        ''' функция удаляет все данные из таблицы, закрывает, и создает заново  '''
        self.table_history.setRowCount(0)
        delete_all()

    def delete(self):
        items_for_delete = self.table_history.selectedItems()
        for i in items_for_delete:
            try:
                row = self.table_history.row(i)
                delete_selected_row(self.table_history.item(row, 0).text())
                self.table_history.removeRow(row)
            except RuntimeError:
                continue
        self.table_history.clearSelection()

    def create_table(self):
        self.table_history.setRowCount(0)
        self.data = show_all_history()
        for i in self.data:
            # создаем таблицу в QWidget
            rows = self.table_history.rowCount()
            self.table_history.setRowCount(rows + 1)
            self.table_history.setItem(rows, 0, QTableWidgetItem(str(i[0])))
            self.table_history.setItem(rows, 1, QTableWidgetItem(str(i[1])))
            self.table_history.setItem(rows, 2, QTableWidgetItem(str(i[2])))
            self.table_history.setItem(rows, 3, QTableWidgetItem(str(i[3])))
            self.table_history.setItem(rows, 4, QTableWidgetItem(str(i[4])))
        self.table_history.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
