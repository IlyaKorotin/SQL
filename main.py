import sys
import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets

from ui import Ui_MainWindow

import matplotlib.pyplot as plt


class Example(QtWidgets.QMainWindow):
    def __init__(self) -> object:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUI()
        self.ui.show_but.clicked.connect(self.but_get)
        self.ui.add_but.clicked.connect(self.but_add)
        self.ui.del_but.clicked.connect(self.but_del)
        self.ui.plot_but_1.clicked.connect(self.but_plot_1)
        self.ui.plot_but_2.clicked.connect(self.but_plot_2)
        self.ui.plot_but_3.clicked.connect(self.but_plot_3)

    def initUI(self):
        global cursor
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        self.input_to_my_db("crebas2.sql")
        self.input_to_my_db("testdata2.sql")

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        for el in tables:
            self.ui.tablelist.addItem(el[0])

    def input_to_my_db(self, name_file):
        sql_lite = open(name_file)
        sql_as_string = sql_lite.read()
        cursor.executescript(sql_as_string)

    def but_get(self):
        name_tbl = self.ui.tablelist.currentText()
        cursor.execute(f"SELECT * FROM {name_tbl}")
        self.put_data_to_table()

    def put_data_to_table(self):
        self.ui.data_here.clear()
        tbl_data = cursor.fetchall()
        num = len(tbl_data[0])

        self.ui.data_here.setRowCount(len(tbl_data))
        self.ui.data_here.setColumnCount(num)

        for col in range(num):
            for row, el in enumerate(tbl_data):
                to_cell = QTableWidgetItem(str(el[col]))
                self.ui.data_here.setItem(row, col, to_cell)

        return tbl_data

    def but_add(self):
        name_tbl = self.ui.tablelist.currentText()
        text_add = self.ui.lineEdit.text()

        cursor.execute(f"pragma table_info({name_tbl})")
        tbl_info = cursor.fetchall()

        cursor.execute(f"SELECT MAX({tbl_info[0][1]}) FROM {name_tbl}")
        id_increase = cursor.fetchone()[0] + 1
        cursor.execute(f"INSERT INTO {name_tbl} ({tbl_info[0][1]},{tbl_info[1][1]}) VALUES ({id_increase},'{text_add}')")

        self.ui.data_here.clear()
        cursor.execute(f"SELECT * FROM {name_tbl}")
        self.put_data_to_table()

    def but_del(self):
        try:
            item = self.ui.data_here.currentItem().text()
            name_tbl = self.ui.tablelist.currentText()

            cursor.execute(f"pragma table_info ({name_tbl})")
            tbl_info = cursor.fetchall()

            cursor.execute(f"DELETE  FROM {name_tbl} WHERE {tbl_info[0][1]} = {item}")
            self.but_get()

        except Exception as err:
            err_win = QtWidgets.QMessageBox()
            err_win.setIcon(QtWidgets.QMessageBox.Warning)
            err_win.setText(str(err))
            err_win.setWindowTitle("Error")
            err_win.setStandardButtons(QtWidgets.QMessageBox.Ok)
            err_win.exec_()

    def but_plot_1(self):
        cursor.execute(f"SELECT n.id_n, s.salary FROM salary as s, names as n where n.id_n = s.id_n")
        table_data = self.put_data_to_table()

        plt.xlabel('x')
        plt.ylabel('y')

        x = []
        y = []

        for el in table_data:
            x.append(el[0])
            y.append(el[1])

        size = len(x)
        i = 0
        sum_xy = 0
        sum_y = 0
        sum_x = 0
        sum_x2 = 0
        while i < size:
            sum_xy += x[i] * y[i]
            sum_y += y[i]
            sum_x += x[i]
            sum_x2 += x[i] * x[i]
            i += 1
        a = (size * sum_xy - sum_x * sum_y) / (size * sum_x2 - sum_x * sum_x)
        b = (sum_y - sum_x * a)/size
        y_new = []
        for el in x:
            y_new.append(a * el + b)

        plt.plot(x, y_new, label='линия аппроксимации', c='green')
        plt.scatter(x, y, label="значения", c='purple')
        plt.legend(loc="best")
        plt.show()

    def but_plot_2(self):
        cursor.execute(f"SELECT a.id_a, s.salary FROM salary as s, ages as a where a.id_a = s.id_a")
        table_data = self.put_data_to_table()

        plt.xlabel('x')
        plt.ylabel('y')

        x = []
        y = []

        for el in table_data:
            x.append(el[0])
            y.append(el[1])

        size = len(x)
        i = 0
        sum_xy = 0
        sum_y = 0
        sum_x = 0
        sum_sqare_x = 0
        while i < size:
            sum_xy += x[i] * y[i]
            sum_y += y[i]
            sum_x += x[i]
            sum_sqare_x += x[i] * x[i]
            i += 1
        average_x = sum_x / size
        average_y = sum_y / size
        k = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
        b = average_y - average_x * k
        y_new = []
        for el in x:
            y_new.append(k * el + b)

        plt.plot(x, y_new, label='линия аппроксимации', c='yellow')
        plt.scatter(x, y, label="значения", c='black')
        plt.legend(loc="best")
        plt.show()

    def but_plot_3(self):
        cursor.execute(f"SELECT p.id_p, s.salary FROM salary as s, prem as p where p.id_p = s.id_p")
        table_data = self.put_data_to_table()

        plt.xlabel('x')
        plt.ylabel('y')

        x = []
        y = []

        for el in table_data:
            x.append(el[0])
            y.append(el[1])

        size = len(x)
        i = 0
        sum_xy = 0
        sum_y = 0
        sum_x = 0
        sum_sqare_x = 0
        while i < size:
            sum_xy += x[i] * y[i]
            sum_y += y[i]
            sum_x += x[i]
            sum_sqare_x += x[i] * x[i]
            i += 1
        average_x = sum_x / size
        average_y = sum_y / size
        k = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
        b = average_y - average_x * k
        y_new = []
        for el in x:
            y_new.append(k * el + b)

        plt.plot(x, y_new, label='линия аппроксимации', c='pink')
        plt.scatter(x, y, label="значения", c='gray')
        plt.legend(loc="best")
        plt.show()



app = QtWidgets.QApplication([])
application = Example()
application.show()

sys.exit(app.exec_())
