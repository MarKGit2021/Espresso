import sys

import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        title = ["ID", "название сорта", "степень обжарки",
                 "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        res3 = {i[0]: i[1] for i in cur.execute('SELECT * FROM types').fetchall()}
        res2 = {i[0]: i[1] for i in cur.execute('SELECT * FROM roast').fetchall()}

        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)

            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                if j == 2:
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(res2[elem])))
                if j == 3:
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(res3[elem])))
        self.tableWidget.resizeColumnsToContents()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
