# This Python file uses the following encoding: utf-8
import sys
import csv
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, qApp
from PyQt5 import uic


open('csv_files/result.csv', 'w').close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.breakfast_form = self
        self.dinner_form = self
        self.supper_form = self
        self.result_form = self
        uic.loadUi('ui_files/main.ui', self)
        self.breakfast_btn.clicked.connect(self.add_breakfast)
        self.dinner_btn.clicked.connect(self.add_dinner)
        self.supper_btn.clicked.connect(self.add_supper)
        self.result_btn.clicked.connect(self.result)
        self.label.setVisible(False)
        self.gender = [self.women, self.men]
        self.kfa = [self.kfa_17, self.kfa_13, self.kfa_11]

    def add_breakfast(self):
        self.breakfast_form = Breakfast_dialog()
        self.breakfast_form.show()

    def add_dinner(self):
        self.dinner_form = Dinner_dialog()
        self.dinner_form.show()

    def add_supper(self):
        self.supper_form = Supper_dialog()
        self.supper_form.show()

    def result(self):
        global calories
        calories = 0
        a = 0
        b = 0
        for i in self.gender:
            if i.isChecked():
                a = 1
        for i in self.kfa:
            if i.isChecked():
                b = 1
        if self.weight_line.text().strip() != 0 and self.height_line.text().strip() != 0 and \
                self.weight_line.text().strip() != '' and self.height_line.text().strip() != '' and \
                a == 1 and b == 1:
            for i in self.kfa:
                if i.isChecked():
                    kfa_human = i.text()
                    calories = int((0.063 * float(self.weight_line.text()) + 2.896) * 240 * float(kfa_human))
            self.result_form = Result_dialog()
            self.result_form.show()
            self.label.setVisible(False)
            self.height_line.setEnabled(False)
            self.weight_line.setEnabled(False)
        else:
            self.label.setVisible(True)


class Breakfast_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.add_product_new = self
        uic.loadUi('ui_files/breakfast_dialog.ui', self)
        self.yes_btn.clicked.connect(self.add_product_new_form)
        self.yes_btn.clicked.connect(self.close)
        self.no_btn.clicked.connect(self.close)
        self.ok_btn.clicked.connect(self.add_product)
        self.error_label.setVisible(False)
        self.dialog_label.setVisible(False)
        self.yes_btn.setVisible(False)
        self.no_btn.setVisible(False)
        self.label_3.setVisible(False)

    def add_product(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        row_res = []

        file = open('csv_files/products.csv', 'r')
        reader = csv.reader(file, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            list1.append(row[0])
            list2.append(row[1])
            list3.append(row[2])
            list4.append(row[3])
            list5.append(row[4])
        list1.pop(0), list2.pop(0), list3.pop(0), list4.pop(0), list5.pop(0)
        if self.product.text().strip() in list1:
            index_list = int(list1.index(self.product.text().strip()))
            result = open('csv_files/result.csv', 'r', newline='')
            reader1 = csv.reader(result, delimiter=';', quotechar='"')
            for index1, row1 in enumerate(reader1):
                row_res.append(row1[0])
            result = open('csv_files/result.csv', 'a', newline='')
            writer = csv.writer(result, delimiter=';', quotechar='"')
            if self.product.text().strip() in row_res:
                self.label_3.setVisible(True)
            else:
                writer.writerow((self.product.text().lower().strip(),
                                 float(float(list2[index_list]) / 100 * int(self.m_product.text().strip())),
                                 list3[index_list], list4[index_list], list5[index_list],
                                 int(self.m_product.text().strip())))
                file.close()
                result.close()
                self.close()
                self.label_3.setVisible(False)
        else:
            self.label_3.setVisible(False)
            self.error_label.setVisible(True)
            self.dialog_label.setVisible(True)
            self.yes_btn.setVisible(True)
            self.no_btn.setVisible(True)
            file.close()

    def add_product_new_form(self):
        self.add_product_new = Add_product()
        self.add_product_new.show()


class Dinner_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.add_product_new = self
        uic.loadUi('ui_files/dinner_dialog.ui', self)
        self.yes_btn.clicked.connect(self.add_product_new_form)
        self.yes_btn.clicked.connect(self.close)
        self.no_btn.clicked.connect(self.close)
        self.ok_btn.clicked.connect(self.add_product)
        self.error_label.setVisible(False)
        self.dialog_label.setVisible(False)
        self.yes_btn.setVisible(False)
        self.no_btn.setVisible(False)
        self.label_3.setVisible(False)

    def add_product(self):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        row_res = []

        file = open('csv_files/products.csv', 'r')
        reader = csv.reader(file, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            list1.append(row[0])
            list2.append(row[1])
            list3.append(row[2])
            list4.append(row[3])
            list5.append(row[4])
        list1.pop(0), list2.pop(0), list3.pop(0), list4.pop(0), list5.pop(0)
        if self.product.text().strip() in list1:
            index_list = int(list1.index(self.product.text().strip()))
            result = open('csv_files/result.csv', 'r', newline='')
            reader1 = csv.reader(result, delimiter=';', quotechar='"')
            for index1, row1 in enumerate(reader1):
                row_res.append(row1[0])
            result = open('csv_files/result.csv', 'a', newline='')
            writer = csv.writer(result, delimiter=';', quotechar='"')
            if self.product.text().strip() in row_res:
                self.label_3.setVisible(True)
            else:
                writer.writerow((self.product.text().lower().strip(),
                                 float(float(list2[index_list]) / 100 * int(self.m_product.text().strip())),
                                 list3[index_list], list4[index_list], list5[index_list],
                                 int(self.m_product.text().strip())))
                file.close()
                result.close()
                self.close()
                self.label_3.setVisible(False)
        else:
            self.label_3.setVisible(False)
            self.error_label.setVisible(True)
            self.dialog_label.setVisible(True)
            self.yes_btn.setVisible(True)
            self.no_btn.setVisible(True)
            file.close()

    def add_product_new_form(self):
        self.add_product_new = Add_product()
        self.add_product_new.show()


class Supper_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.add_product_new = self
        uic.loadUi('ui_files/supper_dialog.ui', self)
        self.yes_btn.clicked.connect(self.add_product_new_form)
        self.yes_btn.clicked.connect(self.close)
        self.no_btn.clicked.connect(self.close)
        self.ok_btn.clicked.connect(self.add_product)
        self.error_label.setVisible(False)
        self.dialog_label.setVisible(False)
        self.yes_btn.setVisible(False)
        self.no_btn.setVisible(False)
        self.label_3.setVisible(False)

    def add_product(self):
        products = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        row_res = []

        products.append(self.product.text())
        products.append(self.m_product.text())
        self.products.addItems(products)
        file = open('csv_files/products.csv', 'r')
        reader = csv.reader(file, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            list1.append(row[0])
            list2.append(row[1])
            list3.append(row[2])
            list4.append(row[3])
            list5.append(row[4])
        list1.pop(0), list2.pop(0), list3.pop(0), list4.pop(0), list5.pop(0)
        if self.product.text().strip() in list1:
            index_list = int(list1.index(self.product.text().strip()))
            result = open('csv_files/result.csv', 'r', newline='')
            reader1 = csv.reader(result, delimiter=';', quotechar='"')
            for index1, row1 in enumerate(reader1):
                row_res.append(row1[0])
            result = open('csv_files/result.csv', 'a', newline='')
            writer = csv.writer(result, delimiter=';', quotechar='"')
            if self.product.text().strip() in row_res:
                self.label_3.setVisible(True)
            else:
                writer.writerow((self.product.text().lower().strip(),
                                 float(float(list2[index_list]) / 100 * int(self.m_product.text().strip())),
                                 list3[index_list], list4[index_list], list5[index_list],
                                 int(self.m_product.text().strip())))
                file.close()
                result.close()
                self.close()
                self.label_3.setVisible(False)
        else:
            self.label_3.setVisible(False)
            self.error_label.setVisible(True)
            self.dialog_label.setVisible(True)
            self.yes_btn.setVisible(True)
            self.no_btn.setVisible(True)
            file.close()

    def add_product_new_form(self):
        self.add_product_new = Add_product()
        self.add_product_new.show()


class Add_product(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/add_product.ui', self)
        self.add_btn.clicked.connect(self.add)
        self.add_btn.clicked.connect(self.close)

    def add(self):
        file = open('csv_files/products.csv', 'a', newline='')
        csv_writer = csv.writer(file, delimiter=';', quotechar='"')
        csv_writer.writerow([self.product_name.text().lower().strip(), self.product_calories.text().strip(),
                             self.product_proteins.text().strip(), self.product_fats.text().strip(),
                             self.product_carbohydrates.text().strip()])
        file.close()


class Result_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.open_new_form = self
        uic.loadUi('ui_files/result.ui', self)
        self.close_btn.clicked.connect(self.open_dialog)
        self.dight.setText(str(calories))
        csvfile = open('csv_files/result.csv', 'r')
        reader = csv.reader(csvfile, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        if len(data) > 0:
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))
            self.table.setHorizontalHeaderLabels(['продукт', 'ккал', 'белки', 'жиры', 'углеводы', 'масса'])
            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(item)
                    self.table.setItem(row, col, cellinfo)
                    col += 1

                row += 1
        summ = []
        file = open('csv_files/result.csv', 'r')
        reader = csv.reader(file, delimiter=';')
        for i in reader:
            summ.append(i[1].replace(",", "."))
        summ = map(float, summ)
        self.need.setText(str(round(math.fsum(summ))))
        file.close()

        file = open('csv_files/result.csv', 'r')
        reader = csv.reader(file, delimiter=';')
        summ = []
        for i in reader:
            summ.append(i[2].replace(",", "."))
        summ = map(float, summ)
        self.proteins.setText(str(round(math.fsum(summ))))
        file.close()

        file = open('csv_files/result.csv', 'r')
        reader = csv.reader(file, delimiter=';')
        summ = []
        for i in reader:
            summ.append(i[3].replace(",", "."))
        summ = map(float, summ)
        self.fats.setText(str(round(math.fsum(summ))))
        file.close()

        file = open('csv_files/result.csv', 'r')
        reader = csv.reader(file, delimiter=';')
        summ = []
        for i in reader:
            summ.append(i[4].replace(",", "."))
        summ = map(float, summ)
        self.carbohydrates.setText(str(round(math.fsum(summ))))
        file.close()

    def open_dialog(self):
        self.open_new_form = Dialog()
        self.open_new_form.show()


class Dialog(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/dialog.ui', self)
        self.ok_btn.clicked.connect(qApp.quit)
        self.no_btn.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
