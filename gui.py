from group import *
import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QHBoxLayout, QTableWidgetItem
from student import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

with open('Interface/stylesheet.TXT', 'r', encoding='UTF8') as f:
    them = json.load(f)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_add_student = QtWidgets.QPushButton(self.centralwidget)
        self.b_add_student.setGeometry(QtCore.QRect(79, 169, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_add_student.setFont(font)
        self.b_add_student.setStyleSheet(them["buttons"])
        self.b_add_student.setObjectName("b_add_student")
        self.b_remove_student = QtWidgets.QPushButton(self.centralwidget)
        self.b_remove_student.setGeometry(QtCore.QRect(79, 259, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_remove_student.setFont(font)
        self.b_remove_student.setStyleSheet(them["buttons"])
        self.b_remove_student.setObjectName("b_remove_student")
        self.b_search_student = QtWidgets.QPushButton(self.centralwidget)
        self.b_search_student.setGeometry(QtCore.QRect(79, 349, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_search_student.setFont(font)
        self.b_search_student.setStyleSheet(them["buttons"])
        self.b_search_student.setObjectName("b_search_student")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_list_all = QtWidgets.QPushButton(self.centralwidget)
        self.b_list_all.setGeometry(QtCore.QRect(599, 259, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_list_all.setFont(font)
        self.b_list_all.setStyleSheet(them["buttons"])
        self.b_list_all.setObjectName("b_list_all")
        self.b_remove_group = QtWidgets.QPushButton(self.centralwidget)
        self.b_remove_group.setGeometry(QtCore.QRect(599, 349, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_remove_group.setFont(font)
        self.b_remove_group.setStyleSheet(them["buttons"])
        self.b_remove_group.setObjectName("b_remove_group")
        self.b_exit = QtWidgets.QPushButton(self.centralwidget)
        self.b_exit.setGeometry(QtCore.QRect(405, 450, 171, 71))
        self.b_exit.setStyleSheet(them["buttons"])
        self.b_exit.setObjectName("b_exit")

        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(990, 90, 48, 48))
        self.settings.setStyleSheet(them["buttons"])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"Interface\Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(26, 26))
        self.settings.setObjectName("settings")
        self.b_search_group = QtWidgets.QPushButton(self.centralwidget)
        self.b_search_group.setGeometry(QtCore.QRect(600, 170, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_search_group.setFont(font)
        self.b_search_group.setStyleSheet(them["buttons"])
        self.b_search_group.setObjectName("b_search_group")
        self.t_menu = QtWidgets.QLabel(self.centralwidget)
        self.t_menu.setGeometry(QtCore.QRect(450, 60, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(25)
        self.t_menu.setFont(font)
        self.t_menu.setStyleSheet(them['text'])
        self.t_menu.setObjectName("t_menu")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-20, -10, 1131, 861))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(them["background"])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.b_add_student.raise_()
        self.b_remove_student.raise_()
        self.b_search_student.raise_()
        self.b_list_all.raise_()
        self.b_remove_group.raise_()
        self.b_exit.raise_()
        self.settings.raise_()
        self.b_search_group.raise_()
        self.t_menu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.b_add_student.clicked.connect(lambda: self.add_student(MainWindow))
        self.b_remove_student.clicked.connect(self.remove_student)
        self.b_exit.clicked.connect(self.exit_program)
        self.b_search_student.clicked.connect(self.search)
        self.settings.clicked.connect(self.open_settings)
        self.b_list_all.clicked.connect(self.list_all)
        self.b_search_group.clicked.connect(self.open_group)
        self.b_remove_group.clicked.connect(self.open_delete_group)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система контролю успішності студентів"))
        self.b_add_student.setText(_translate("MainWindow", "Додати студента"))
        self.b_remove_student.setText(_translate("MainWindow", "Вилучити студента"))
        self.b_search_student.setText(_translate("MainWindow", "Режим редагування"))
        self.b_list_all.setText(_translate("MainWindow", "Список всіх студентів"))
        self.b_remove_group.setText(_translate("MainWindow", "Видалити групу"))
        self.b_exit.setText(_translate("MainWindow", "Вийти з програми"))
        self.b_search_group.setText(_translate("MainWindow", "Пошук групи"))
        self.t_menu.setText(_translate("MainWindow", "Меню"))
    def list_all(self):
        MainWindow.hide()
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_list_all()
        self.ui.setupUi(self.second_window,MainWindow)
        self.second_window.show()
    def remove_student(self):
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_remove_student()
        self.ui.setupUi(self.second_window,MainWindow)
        self.second_window.show()
    def exit_program(self):
        sys.exit()
    def add_student(self,MainWindow):
        MainWindow.hide()
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_add_student()
        self.ui.setupUi(self.second_window,MainWindow)
        self.second_window.show()
    def search(self):
        MainWindow.hide()
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_edit_students()
        self.ui.setupUi(self.second_window,MainWindow)
        self.second_window.show()
    def open_settings(self):
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_settings()
        self.ui.setupUi(self.second_window,MainWindow)
        self.second_window.show()
    def open_group(self):
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_search_group()
        self.ui.setupUi(self.second_window, MainWindow)
        self.second_window.show()
    def open_delete_group(self):
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_delete_group()
        self.ui.setupUi(self.second_window, MainWindow)
        self.second_window.show()
class Ui_add_student(object):
    def setupUi(self, add_student,MainWindow):
        add_student.setObjectName("add_student")
        add_student.resize(522, 432)
        add_student.setMinimumSize(QtCore.QSize(470, 440))
        add_student.setMaximumSize(QtCore.QSize(470, 440))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        add_student.setFont(font)
        add_student.setIconSize(QtCore.QSize(46, 46))
        self.centralwidget = QtWidgets.QWidget(add_student)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(112, 89, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(them["line"])
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(112, 139, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(them["line"])
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(112, 189, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(them["line"])
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(112, 289, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(them["line"])
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.b_add = QtWidgets.QPushButton(self.centralwidget)
        self.b_add.setGeometry(QtCore.QRect(130, 360, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_add.setFont(font)
        self.b_add.setStyleSheet(them['buttons'])
        self.b_add.setObjectName("b_add")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(112, 239, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(them["line"])
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(30, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them['buttons'])
        self.b_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"Interface\i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(170, 50, 140, 16))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 100, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("color:black")
        self.label_text.setObjectName("label_text")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(them['text2'])
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 150, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(them['text2'])
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 200, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(them['text2'])
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 250, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(them['text2'])
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 300, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(them['text2'])
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-90, -20, 691, 521))
        self.label_3.setStyleSheet(them['background'])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.b_add.raise_()
        self.lineEdit_5.raise_()
        self.b_back.raise_()
        self.label_text.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        add_student.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_student)
        QtCore.QMetaObject.connectSlotsByName(add_student)
        self.b_add.clicked.connect(self.complete)
        self.b_back.clicked.connect(lambda: self.back_menu(add_student,MainWindow))
    def retranslateUi(self, add_student):
        _translate = QtCore.QCoreApplication.translate
        add_student.setWindowTitle(_translate("add_student", "Додати Студента"))
        self.b_add.setText(_translate("MainWindow", "Додати студента"))
        self.label_text.setText(_translate("MainWindow", "Ви добавили студента"))
        self.label_6.setText(_translate("MainWindow", "Введіть ім\'я!"))
        self.label_7.setText(_translate("MainWindow", "Введіть Фамілію!"))
        self.label_8.setText(_translate("MainWindow", "Введіть по батькові!"))
        self.label_9.setText(_translate("MainWindow", "Введіть групу!"))
        self.label_10.setText(_translate("MainWindow", "Введіть бал!"))
        self.lineEdit.setPlaceholderText("Введіть ім'я студента")
        self.lineEdit_2.setPlaceholderText("Введіть прізвище студента")
        self.lineEdit_3.setPlaceholderText("Введіть по батькові студента")
        self.lineEdit_4.setPlaceholderText("Введіть групу студента")
        self.lineEdit_5.setPlaceholderText("Введіть середній бал студента")
        self.label_10.hide()
        self.label_text.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
    def back_menu(self,CurrentWindow,MainWindow):
        CurrentWindow.close()
        MainWindow.show()

    def complete(self):
        studentName = self.lineEdit.text()
        studentSurname = self.lineEdit_2.text()
        studentPatronymic = self.lineEdit_3.text()
        studentGroup = self.lineEdit_4.text()
        studentAvgScore = self.lineEdit_5.text()
        if studentName.strip() and studentSurname.strip() and studentPatronymic.strip() and studentGroup.strip() and studentAvgScore != '':
            # перевірка на наявність студента з такими ж іменем, прізвищем, по-батькові
            with open('Students/students.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                fields = line.strip().lower().split(', ')
                if (fields[0] == studentName.lower() and fields[1] == studentSurname.lower() and fields[2] == studentPatronymic.lower()):
                    be = True
                    break
                else:
                    be = False
            if be == False:
                if studentAvgScore.isdigit() and 1 <= int(studentAvgScore) <= 12:
                    student = Student(studentName, studentSurname, studentPatronymic, studentGroup, studentAvgScore)
                    student.addStudent()
                    self.label_text.show()
                else:
                    QMessageBox.warning(None, 'Помилка', 'Середня оцінка має бути числом від 1 до 12!')
                    self.label_text.hide()
            else:
                QMessageBox.warning(None, 'Помилка', 'Такий студент вже існує!')
                self.label_text.hide()
        if studentName.strip() and studentSurname.strip() and  studentPatronymic.strip() and studentGroup.strip() and  studentAvgScore.strip() == '':
            self.label_text.hide()
        if studentName.strip() == '':
            self.label_6.show()
        else:
            self.label_6.hide()

        if studentSurname.strip() == '':
            self.label_7.show()
        else:
            self.label_7.hide()

        if studentPatronymic.strip() == '':
            self.label_8.show()
        else:
            self.label_8.hide()
        if studentGroup.strip() == '':
            self.label_10.show()
        else:
            self.label_10.hide()
        if studentAvgScore.strip() == '':
            self.label_9.show()
        else:
            self.label_9.hide()
class Ui_remove_student(object):
    def setupUi(self, remove_student,MainWindow):
        remove_student.setObjectName("remove_student")
        remove_student.resize(593, 439)
        remove_student.setMinimumSize(QtCore.QSize(0, 0))
        remove_student.setMaximumSize(QtCore.QSize(593, 475))
        self.centralwidget = QtWidgets.QWidget(remove_student)
        self.centralwidget.setMinimumSize(QtCore.QSize(20, 20))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-150, -20, 1111, 641))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(them['background'])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(them['line'])
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введіть інформацію про студента")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 90, 121, 31))
        self.pushButton.setStyleSheet(them["buttons"])
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(410, 140, 121, 31))
        self.pushButton2.setStyleSheet(them["buttons"])
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 20, 35, 35))
        self.pushButton_3.setStyleSheet(them["buttons"])
        self.pushButton_3.setObjectName("pushButton_3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(them["text"])
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.i = 0
        self.comboBox.setGeometry(QtCore.QRect(40, 140, 351, 31))
        #self.comboBox.setStyleSheet(them['box'])
        self.comboBox.setObjectName("comboBox")
        remove_student.setCentralWidget(self.centralwidget)

        self.retranslateUi(remove_student)
        QtCore.QMetaObject.connectSlotsByName(remove_student)
        self.pushButton.clicked.connect(self.search)
        self.pushButton2.clicked.connect(self.delete_student)
        self.pushButton_3.clicked.connect(lambda: self.back_menu(remove_student,MainWindow))
    def retranslateUi(self, remove_student):
        _translate = QtCore.QCoreApplication.translate
        remove_student.setWindowTitle(_translate("remove_student", "Видалити студента"))
        self.pushButton.setText(_translate("MainWindow", "Пошук"))
        self.pushButton2.setText(_translate("MainWindow", "Видалити"))
        self.label.setText(_translate("MainWindow", "Видалення студента"))
    def search(self):
        self.comboBox.clear()
        Search = self.lineEdit.text()
        self.results = Student.find_Student(Search)
        for i in range(len(self.results)):
            self.comboBox.addItems([self.results[i]])
    def delete_student(self):
        self.delet = self.comboBox.currentText()
        if self.comboBox.currentText() != '':
            choice = QMessageBox.question(None, 'Підтвердження вибору', f'Ви точно хочете видалити : {self.comboBox.currentText()}?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if choice == QMessageBox.Yes:
                Student.removeStudent(self.delet)
                self.comboBox.clear()

    def back_menu(self, CurrentWindow, MainWindow):
        CurrentWindow.close()
        MainWindow.show()
class Ui_edit_students(object):
    def setupUi(self, edit_students,MainWindow):
        edit_students.setObjectName("edit_students")

        edit_students.resize(674, 601)
        edit_students.setMinimumSize(QtCore.QSize(674, 601,))
        edit_students.setMaximumSize(QtCore.QSize(674, 601,))
        self.centralwidget = QtWidgets.QWidget(edit_students)
        self.centralwidget.setMinimumSize(QtCore.QSize(20, 20))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-200, -40, 1111, 771))
        font = QtGui.QFont()
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(580, 170, 41, 41))
        font.setFamily("MS PGothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(them["background"])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 371, 31))
        self.lineEdit.setStyleSheet(them["line"])
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 160, 517, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("text-mergin:10px;")
        self.tableWidget_2.setAutoScrollMargin(22)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(580, 170, 41, 41))
        self.Add_button.setStyleSheet(them["buttons"])
        self.Add_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_button.setIcon(icon)
        self.Add_button.setIconSize(QtCore.QSize(57, 57))
        self.Add_button.setObjectName("Add_button")
        self.Delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_button.setGeometry(QtCore.QRect(580, 350, 41, 41))
        self.Delete_button.setStyleSheet(them["buttons"])
        self.Delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Interface/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete_button.setIcon(icon1)
        self.Delete_button.setIconSize(QtCore.QSize(71, 71))
        self.Delete_button.setObjectName("Delete_button")
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(410, 90, 121, 31))
        self.Search_button.setStyleSheet(them["buttons"])
        self.Search_button.setObjectName("Search_button")
        self.Edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Edit_button.setGeometry(QtCore.QRect(580, 260, 41, 41))
        self.Edit_button.setStyleSheet(them["buttons"])
        self.Edit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Interface/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Edit_button.setIcon(icon2)
        self.Edit_button.setIconSize(QtCore.QSize(71, 71))
        self.Edit_button.setObjectName("Edit_button")
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(20, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them["buttons"])
        self.b_back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon3)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        edit_students.setCentralWidget(self.centralwidget)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.last = None
        self.i = 0
        self.tableWidget_2.horizontalHeader().sectionClicked.connect(self.sort)
        self.retranslateUi(edit_students)
        QtCore.QMetaObject.connectSlotsByName(edit_students)
        self.ui_add_student = Ui_add_student()
        self.b_back.clicked.connect(lambda: self.back_menu(edit_students,MainWindow))
        self.Add_button.clicked.connect(self.add_student_dialog)
        self.Edit_button.clicked.connect(self.edit_student_dialog)
        self.update_list()
        self.Delete_button.clicked.connect(self.delete_row)
        self.Search_button.clicked.connect(self.search)
    def retranslateUi(self, edit_students):
        _translate = QtCore.QCoreApplication.translate
        edit_students.setWindowTitle(_translate("edit_students", "Редагування"))
        self.label.setText(_translate("edit_students", "Редагування"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("edit_students", "Ім\'я"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("edit_students", "Прізвище"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("edit_students", "По батькові"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("edit_students", "Група"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("edit_students", "Середній бал"))
        self.Search_button.setText(_translate("edit_students", "Знайти"))

    def search(self):
        def search(self):
            Search = self.lineEdit.text()
            self.results = Student.find_Student(Search)
            self.tableWidget_2.setRowCount(len(self.results))
            for i in range(len(self.results)):
                line = self.results[i].split(', ')
                for j in range(len(line)):
                    item = QtWidgets.QTableWidgetItem(line[j])
                    self.tableWidget_2.setItem(i, j, item)

    def sort(self, index):
        column = index  # індекс стовпця, за яким відбуватиметься сортування
        my_array = []  # ініціалізуємо масив, в якому зберігатимуться значення рядків таблиці

        # Якщо це 4 рядок
        if column == 4:
            if not hasattr(self, 'reverse_sort'):  # перевіряємо, чи визначено атрибут reverse_sort
                self.reverse_sort = False
            self.reverse_sort = not self.reverse_sort  # змінюємо порядок сортування на протилежний
            for row in range(self.tableWidget_2.rowCount()):  # перебираємо всі рядки таблиці
                row_values = []  # ініціалізуємо масив, в якому зберігатимуться значення стовпців рядка
                for column in range(self.tableWidget_2.columnCount()):  # перебираємо всі стовпці рядка
                    item = self.tableWidget_2.item(row, column)  # отримуємо значення комірки таблиці
                    if item is not None:  # якщо значення комірки не дорівнює None
                        row_values.append(item.text())  # додаємо значення комірки в масив
                my_array.append(row_values)  # додаємо масив значень стовпців рядка в загальний масив my_array
            my_array.sort(key=lambda x: int(x[4]),
                          reverse=self.reverse_sort)  # сортуємо масив my_array за значенням 4-го стовпця в порядку зростання або спадання в залежності від значення змінної reverse_sort
            self.tableWidget_2.setRowCount(
                len(my_array))  # встановлюємо кількість рядків у таблиці відповідно до кількості рядків у масиві my_array
            for i in range(len(my_array)):  # перебираємо всі рядки у масиві my_array
                row = my_array[i]  # отримуємо рядок
                for j in range(len(row)):
                    item = QtWidgets.QTableWidgetItem(row[j])
                    self.tableWidget_2.setItem(i, j, item) # записуємо значення з масива у таблицю
        else:
            if colum == self.last:
                self.sort_order = QtCore.Qt.DescendingOrder if self.sort_order == QtCore.Qt.AscendingOrder else QtCore.Qt.AscendingOrder
            else:
                self.sort_order = QtCore.Qt.AscendingOrder
            self.tableWidget_2.sortItems(colum, self.sort_order)
            # Оновити значення last (останнього стовпця), щоб при наступному кліку на цей же стовпець можна було встановити правильний порядок сортування.
            self.last = colum
    def delete_row(self):
        res = ''
        row_values = []
        # Отримання індексу виділеного рядка.
        current_row = self.tableWidget_2.currentRow()
        if current_row >= 0:
            # Створення об'єкта Student.
            column_count = self.tableWidget_2.columnCount()

            # Ітерування через усі стовпці та встановлення значень полів об'єкта Student.
            for column in range(column_count):
                item = self.tableWidget_2.item(current_row, column)
                if item is not None:
                    row_values.append(item.text())

            result = (', '.join(row_values))
            # Видалення студента з бази даних.
            Student.removeStudent(result)

            # Видалення виділеного рядка з таблиці.
            self.tableWidget_2.removeRow(current_row)

    def update_list(self):
        f = open('Students/students.txt', 'r', encoding='UTF8').read().split('\n')
        self.tableWidget_2.setRowCount(len(f) - 1)
        for i in range(len(f)):
            line = f[i].split(', ')
            for j in range(len(line)):
                item = QtWidgets.QTableWidgetItem(line[j])
                self.tableWidget_2.setItem(i, j, item)
    def add(self):
        MainWindow.hide()
        self.second_window = QtWidgets.QMainWindow()
        self.ui = Ui_add_student()
        self.ui.setupUi(self.second_window, MainWindow)
        self.second_window.show()
    def back_menu(self, CurrentWindow, MainWindow):
        CurrentWindow.close()
        MainWindow.show()
    def edit_student_dialog(self):
        edit_student = []
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Add Student")
        dialog.setModal(True)
        dialog.resize(300, 200)
        res = ''
        row_values = []
        # Отримання індексу виділеного рядка.
        current_row = self.tableWidget_2.currentRow()
        if current_row >= 0:
            # Створення об'єкта Student.
            column_count = self.tableWidget_2.columnCount()

            # Ітерування через усі стовпці та встановлення значень полів об'єкта Student.
            for column in range(column_count):
                item = self.tableWidget_2.item(current_row, column)
                if item is not None:
                    row_values.append(item.text())
            result = (', '.join(row_values))
        # Create widgets
        label_name = QtWidgets.QLabel("Ім'я:")
        label_surname = QtWidgets.QLabel("Фамілія:")
        label_patronymic = QtWidgets.QLabel("По батькові:")
        label_group = QtWidgets.QLabel("Група:")
        label_average = QtWidgets.QLabel("Сер.Оцінка:")
        line_name = QtWidgets.QLineEdit()
        line_name.setText(row_values[0])
        line_surname = QtWidgets.QLineEdit()
        line_surname.setText(row_values[1])
        line_patronymic = QtWidgets.QLineEdit()
        line_patronymic.setText(row_values[2])
        line_group = QtWidgets.QLineEdit()
        line_group.setText(row_values[3])
        line_average = QtWidgets.QLineEdit()
        line_average.setText(row_values[4])
        button_add = QtWidgets.QPushButton("Змінити")
        button_cancel = QtWidgets.QPushButton("Відмінити")

        # Add widgets to layout
        layout = QtWidgets.QGridLayout()
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(line_name, 0, 1)
        layout.addWidget(label_surname, 1, 0)
        layout.addWidget(line_surname, 1, 1)
        layout.addWidget(label_patronymic, 2, 0)
        layout.addWidget(line_patronymic, 2, 1)
        layout.addWidget(label_group, 3, 0)
        layout.addWidget(line_group, 3, 1)
        layout.addWidget(label_average, 4, 0)
        layout.addWidget(line_average, 4, 1)
        layout.addWidget(button_add, 5, 0)
        layout.addWidget(button_cancel, 5, 1)
        dialog.setLayout(layout)
        # Connect signals and slots
        button_add.clicked.connect(dialog.accept)
        button_cancel.clicked.connect(dialog.reject)

        # Show the dialog and wait for user response
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            studentName = line_name.text().strip()
            studentSurname = line_surname.text().strip()
            studentPatronymic = line_patronymic.text().strip()
            studentGroup = line_group.text().strip()
            studentAvgScore = line_average.text().strip()
            edit_student += [studentName, studentSurname, studentPatronymic, studentGroup, studentAvgScore]
            #print(current_student)
            if studentName.strip() and studentSurname.strip() and studentPatronymic.strip() and studentGroup.strip() and studentAvgScore != '':
                # перевірка на наявність студента з такими ж іменем, прізвищем, по-батькові
                with open('Students/students.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for line in lines:
                    fields = line.strip().lower().split(', ')
                    if (fields[0] == studentName.lower() and fields[1] == studentSurname.lower() and fields[
                        2] == studentPatronymic.lower()):
                        be = True
                        break
                    else:
                        be = False
                if be == False:
                    if studentAvgScore.isdigit() and 1 <= int(studentAvgScore) <= 12:
                        Student.editStudent(result,edit_student)
                        self.update_list()
                    else:
                        QMessageBox.warning(None, 'Помилка', 'Середня оцінка має бути числом від 1 до 12!')
                else:
                    QMessageBox.warning(None, 'Помилка', 'Такий студент вже існує!')
                    self.add_student_dialog()
            else:
                QMessageBox.warning(None, 'Помилка', 'Введіть інформацію у всі поля!')
                self.add_student_dialog()
    def add_student_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Add Student")
        dialog.setModal(True)
        dialog.resize(300, 200)

        # Create widgets
        label_name = QtWidgets.QLabel("Ім'я:")
        label_surname = QtWidgets.QLabel("Фамілія:")
        label_patronymic = QtWidgets.QLabel("По батькові:")
        label_group = QtWidgets.QLabel("Група:")
        label_average = QtWidgets.QLabel("Сер.Оцінка:")
        line_name = QtWidgets.QLineEdit()
        line_surname = QtWidgets.QLineEdit()
        line_patronymic = QtWidgets.QLineEdit()
        line_group = QtWidgets.QLineEdit()
        line_average = QtWidgets.QLineEdit()
        button_add = QtWidgets.QPushButton("Добавити")
        button_cancel = QtWidgets.QPushButton("Відмінити")

        # Add widgets to layout
        layout = QtWidgets.QGridLayout()
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(line_name, 0, 1)
        layout.addWidget(label_surname, 1, 0)
        layout.addWidget(line_surname, 1, 1)
        layout.addWidget(label_patronymic, 2, 0)
        layout.addWidget(line_patronymic, 2, 1)
        layout.addWidget(label_group, 3, 0)
        layout.addWidget(line_group, 3, 1)
        layout.addWidget(label_average, 4, 0)
        layout.addWidget(line_average, 4, 1)
        layout.addWidget(button_add, 5, 0)
        layout.addWidget(button_cancel, 5, 1)
        dialog.setLayout(layout)

        # Connect signals and slots
        button_add.clicked.connect(dialog.accept)
        button_cancel.clicked.connect(dialog.reject)

        # Show the dialog and wait for user response
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            studentName = line_name.text().strip()
            studentSurname = line_surname.text().strip()
            studentPatronymic = line_patronymic.text().strip()
            studentGroup = line_group.text().strip()
            studentAvgScore = line_average.text().strip()

            if studentName.strip() and studentSurname.strip() and studentPatronymic.strip() and studentGroup.strip() and studentAvgScore != '':
                # перевірка на наявність студента з такими ж іменем, прізвищем, по-батькові
                with open('Students/students.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for line in lines:
                    fields = line.strip().lower().split(', ')
                    if (fields[0] == studentName.lower() and fields[1] == studentSurname.lower() and fields[
                        2] == studentPatronymic.lower()):
                        be = True
                        break
                    else:
                        be = False
                if be == False:
                    if studentAvgScore.isdigit() and 1 <= int(studentAvgScore) <= 12:
                        student = Student(studentName, studentSurname, studentPatronymic, studentGroup, studentAvgScore)
                        student.addStudent()
                        self.update_list()
                    else:
                        QMessageBox.warning(None, 'Помилка', 'Середня оцінка має бути числом від 1 до 12!')
                else:
                    QMessageBox.warning(None, 'Помилка', 'Такий студент вже існує!')
                    self.add_student_dialog()
            else:
                QMessageBox.warning(None, 'Помилка', 'Введіть інформацію у всі поля!')
                self.add_student_dialog()
class Ui_list_all(object):
    def setupUi(self, list_all,MainWindow):
        list_all.setObjectName("list_all")
        list_all.resize(641, 585)
        self.centralwidget = QtWidgets.QWidget(list_all)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(80, 60, 501, 481))
        self.tableWidget_2.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(30, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them["buttons"])
        self.b_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-170, -40, 5000, 645))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(them["background"])
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.tableWidget_2.raise_()
        self.b_back.raise_()
        list_all.setCentralWidget(self.centralwidget)
        self.retranslateUi(list_all)
        QtCore.QMetaObject.connectSlotsByName(list_all)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.last_column_clicked = None
        self.i = 0
        self.tableWidget_2.horizontalHeader().sectionClicked.connect(self.on_header_clicked)
        f = open('Students/students.txt', 'r', encoding='UTF8').read().split('\n')
        self.tableWidget_2.setRowCount(len(f)-1)
        for i in range(len(f)):
            line = f[i].split(', ')
            for j in range(len(line)):
                item = QtWidgets.QTableWidgetItem(line[j])
                self.tableWidget_2.setItem(i, j, item)
        self.b_back.clicked.connect(lambda: self.back_menu(list_all,MainWindow))
    def retranslateUi(self, list_all):
        _translate = QtCore.QCoreApplication.translate
        list_all.setWindowTitle(_translate("list_all", "MainWindow"))
        self.label.setText(_translate("list_all", "Список всіх студентів"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("list_all", "Ім\'я"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("list_all", "Прізвище"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("list_all", "По батькові"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("list_all", "Група"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("list_all", "Середній бал"))
    def on_header_clicked(self, index):
        current_column_clicked = index
        if current_column_clicked == self.last_column_clicked:
            self.sort_order = QtCore.Qt.DescendingOrder if self.sort_order == QtCore.Qt.AscendingOrder else QtCore.Qt.AscendingOrder
        else:
            self.sort_order = QtCore.Qt.AscendingOrder
        self.tableWidget_2.sortItems(current_column_clicked, self.sort_order)
        self.last_column_clicked = current_column_clicked
    def back_menu(self,CurrentWindow,MainWindow):
        CurrentWindow.close()
        MainWindow.show()
class Ui_settings(object):
    def setupUi(self, settings,MainWindow):
        settings.setObjectName("settings")
        settings.resize(541, 391)
        settings.setMinimumSize(QtCore.QSize(541, 391))
        settings.setMaximumSize(QtCore.QSize(541, 391))
        self.pushButton = QtWidgets.QPushButton(settings)
        self.pushButton.setGeometry(QtCore.QRect(180, 100, 161, 51))
        self.pushButton.setStyleSheet(them["buttons"])
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(settings)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 161, 51))
        self.pushButton_2.setStyleSheet(them["buttons"])
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(settings)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 240, 161, 51))
        self.pushButton_3.setStyleSheet(them["buttons"])
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(160, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(settings)
        self.label_2.setGeometry(QtCore.QRect(-40, -30, 621, 481))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(them["background"])
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.b_back = QtWidgets.QPushButton(settings)
        self.b_back.setGeometry(QtCore.QRect(20, 30, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them["buttons"])
        self.b_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.b_back.raise_()
        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)
        self.pushButton.clicked.connect(self.change_color)
        self.b_back.clicked.connect(lambda: self.back_menu(settings, MainWindow))
    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Настройки"))
        self.pushButton.setText(_translate("settings", "Змінити колір"))
        self.pushButton_2.setText(_translate("settings", "Очистити все"))
        self.pushButton_3.setText(_translate("settings", "Про автора"))
        self.label.setText(_translate("settings", "Налаштування"))
    def change_color(self):
        dialog = MyDialog()
        dialog.exec_()
    def back_menu(self,CurrentWindow,MainWindow):
        CurrentWindow.close()
        MainWindow.show()
class MyDialog(QDialog):
    def __init__(self):
        green_theme = {
                "buttons": "QPushButton {\n"
"    background-color: rgb(68, 188, 8); \n"
"    border-radius: 15;\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#5adb5e ;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(244, 213, 86);\n"
"}\n"
"",
                "background": "background-color:rgb(207, 255, 170)",
                "text": "color:rgb(0, 0, 0)",
                "text2": "color:rgb(255, 0, 4)",
                "line": "border-radius: 10px;\n"
"border: 2px solid #000000 ;\n"
"\n"
"",
                "edit_button": "QPushButton {\n"
"    background-color: rgb(68, 188, 8); \n"
"    border-radius: 15;\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#5adb5e ;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(244, 213, 86);\n"
"}\n"
""
            }
        gray_theme = {
                "buttons": "QPushButton {\n"
"   appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: rgb(61, 61, 61);\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
"",
                "background": "background-color:rgb(179, 179, 179)",
                "text": "color:rgb(68, 68, 68)",
                "text2": "color:rgb(6, 255, 174)",
                "line": "border-radius: 10px;\n"
                    "border: 2px solid #4676D7 ;\n"
                    "\n"
                    "",
                "edit_button": "QPushButton {\n"
"   appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: #4676D7;\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
""
                     }
        yellow_theme ={
                "buttons": "QPushButton {\n"
"   appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: #4676D7;\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
"",
                "background": "background-color:rgb(229, 249, 255)",
                "text": "color:rgb(223, 255, 174)",
                "text2": "color:rgb(6, 255, 174)",
                "line": "border-radius: 10px;\n"
                    "border: 2px solid #4676D7 ;\n"
                    "\n"
                    "",
                "edit_button": "QPushButton {\n"
"   appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: #4676D7;\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
""}
        blue_theme = {
                "buttons": "QPushButton {\n"
"  appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: #4676D7;\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
"",
                "background": "background-color:rgb(229, 249, 255)",
                "text": "color:rgb(0, 0, 0)",
                "text2": "color:rgb(255, 0, 4)",
                "line": "border-radius: 10px;\n"
                    "border: 2px solid #4676D7 ;\n"
                    "\n"
                    "",
                "edit_button": "QPushButton {\n"
"   appearance: none;\n"
"  border: 0;\n"
"  border-radius: 5px;\n"
"  background: #4676D7;\n"
"  color: #fff;\n"
"  padding: 8px 16px;\n"
"  font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#4616D7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4676D7;\n"
"}\n"
"\n"
"\n"
""

            }


        super().__init__()
        self.setFixedSize(350, 150)  # Встановлення фіксованого розміру вікна
        self.setWindowTitle("Вибір теми")  # Встановлення тексту зверху
        font = QFont()
        font.setPointSize(9)
        label = QLabel("Вибір теми", self)
        label.setFont(font)
        label.move(100, 20)
        button1 = QPushButton("", self)
        button1.setStyleSheet("background-color: #118c67;")
        button2 = QPushButton("", self)
        button2.setStyleSheet("background-color: #444654;")
        button3 = QPushButton("", self)
        button3.setStyleSheet("background-color: #abac3f;")
        button4 = QPushButton("", self)
        button4.setStyleSheet("background-color: #3f56ac;")
        # Встановлення фіксованого розміру кнопок
        button_size = 60
        button1.setFixedSize(button_size, button_size)
        button2.setFixedSize(button_size, button_size)
        button3.setFixedSize(button_size, button_size)
        button4.setFixedSize(button_size, button_size)
        button4.clicked.connect(lambda: self.blue_color(blue_theme))
        button3.clicked.connect(lambda: self.yellow_color(yellow_theme))
        button2.clicked.connect(lambda: self.gray_color(gray_theme))
        button1.clicked.connect(lambda: self.green_color(green_theme))
        # Додавання кнопок до макету
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        self.setLayout(layout)

    def blue_color(self, current_theme):
        print("blue")
        choice = QMessageBox.question(None, 'Підтвердження вибору',
                                      f'Ви точно хочете змінити колір? Програму треба буде запустити ще раз!',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            with open('Interface/stylesheet.TXT', 'w', encoding='UTF8') as f:
                f.write(json.dumps(current_theme))
            sys.exit()
    def green_color(self,current_theme):
        print("green")
        choice = QMessageBox.question(None, 'Підтвердження вибору',
                                      f'Ви точно хочете змінити колір? Програму треба буде запустити ще раз!',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            with open('Interface/stylesheet.TXT', 'w', encoding='UTF8') as f:
                f.write(json.dumps(current_theme))
            sys.exit()
    def yellow_color(self,current_theme):
        print("yellow")
        choice = QMessageBox.question(None, 'Підтвердження вибору',
                                      f'Ви точно хочете змінити колір? Програму треба буде запустити ще раз!',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            with open('Interface/stylesheet.TXT', 'w', encoding='UTF8') as f:
                f.write(json.dumps(current_theme))
            sys.exit()
    def gray_color(self,current_theme):
        print("gray")
        choice = QMessageBox.question(None, 'Підтвердження вибору',
                                      f'Ви точно хочете змінити колір? Програму треба буде запустити ще раз!',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            with open('Interface/stylesheet.TXT', 'w', encoding='UTF8') as f:
                f.write(json.dumps(current_theme))
            sys.exit()
class Ui_search_group(object):
    def setupUi(self, search_group,MainWindow):
        search_group.setObjectName("search_group")
        search_group.resize(571, 601)
        search_group.setMinimumSize(QtCore.QSize(0, 0))
        search_group.setMaximumSize(QtCore.QSize(10000, 100000))
        self.centralwidget = QtWidgets.QWidget(search_group)
        self.centralwidget.setMinimumSize(QtCore.QSize(20, 20))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-200, -40, 1111, 771))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(them["background"])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 90, 371, 31))
        #self.comboBox.setStyleSheet(them["line"])
        self.comboBox.setObjectName("comboBox")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 140, 501, 461))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("text-mergin:10px;")
        self.tableWidget_2.setAutoScrollMargin(22)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(430, 90, 101, 31))
        self.Search_button.setStyleSheet(them["buttons"])
        self.Search_button.setObjectName("Search_button")
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(20, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them["buttons"])
        self.b_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        search_group.setCentralWidget(self.centralwidget)

        self.retranslateUi(search_group)
        QtCore.QMetaObject.connectSlotsByName(search_group)
        group = Group('','','','','')
        results = group.findGroup()
        for i in range(len(results)):
            self.comboBox.addItems([results[i]])
        self.Search_button.clicked.connect(lambda: self.list(results,group))
        self.b_back.clicked.connect(lambda: self.back_menu(search_group, MainWindow))
    def retranslateUi(self, search_group):
        _translate = QtCore.QCoreApplication.translate
        search_group.setWindowTitle(_translate("search_group", "Пошук групи"))
        self.label.setText(_translate("search_group", "Знайти групу"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("search_group", "Ім\'я"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("search_group", "Прізвище"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("search_group", "По батькові"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("search_group", "Група"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("search_group", "Середній бал"))
        self.Search_button.setText(_translate("search_group", "Знайти"))
    def list(self,results,group):
        num = self.comboBox.currentIndex()
        students = group.listStudents(results,num)
        self.tableWidget_2.setRowCount(len(students))
        self.tableWidget_2.setColumnCount(5)
        # проходимося по кожному студенту та додаємо його дані до tableWidget_2
        for i, student in enumerate(students):
            student_data = student.split(", ")
            for j, data in enumerate(student_data):
                item = QTableWidgetItem(data)
                self.tableWidget_2.setItem(i, j, item)
    def back_menu(self,CurrentWindow,MainWindow):
        CurrentWindow.close()
        MainWindow.show()
class Ui_delete_group(object):
    def setupUi(self, delete_group, MainWindow):
        delete_group.setObjectName("delete_group")
        delete_group.resize(532, 300)
        delete_group.setMinimumSize(QtCore.QSize(532, 300))
        delete_group.setMaximumSize(QtCore.QSize(532, 300))
        self.centralwidget = QtWidgets.QWidget(delete_group)
        self.centralwidget.setMinimumSize(QtCore.QSize(20, 20))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-200, -30, 1111, 771))
        self.label_3.setMinimumSize(QtCore.QSize(1111, 771))
        self.label_3.setMaximumSize(QtCore.QSize(1111, 771))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(them["background"])
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 100, 351, 31))
        #self.comboBox.setStyleSheet(them["line"])
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 121, 31))
        self.pushButton_2.setStyleSheet(them["buttons"])
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(20, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.b_back.setFont(font)
        self.b_back.setStyleSheet(them["buttons"])
        self.b_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/i_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_back.setIcon(icon)
        self.b_back.setIconSize(QtCore.QSize(26, 26))
        self.b_back.setObjectName("b_back")
        self.pushButton_2.setObjectName("pushButton_2")
        delete_group.setCentralWidget(self.centralwidget)

        self.retranslateUi(delete_group)
        QtCore.QMetaObject.connectSlotsByName(delete_group)
        group = Group('', '', '', '', '')
        results = group.findGroup()
        for i in range(len(results)):
            self.comboBox.addItems([results[i]])
        self.pushButton_2.clicked.connect(lambda: self.delete(group))
        self.b_back.clicked.connect(lambda: self.back_menu(delete_group, MainWindow))
    def retranslateUi(self, delete_group):
        _translate = QtCore.QCoreApplication.translate
        delete_group.setWindowTitle(_translate("delete_group", "delete_group"))
        self.label.setText(_translate("delete_group", "Видалити групу"))
        self.pushButton_2.setText(_translate("delete_group", "Видалити"))

    def delete(self, group):
        res = self.comboBox.currentText()
        choice = QMessageBox.question(None, 'Підтвердження вибору',
                                      f'Ви точно хочете видалити групу {self.comboBox.currentText()}?',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            group.deleteGroup(res)
            self.comboBox.clear()
            results = group.findGroup()
            for i in range(len(results)):
                self.comboBox.addItems([results[i]])
            self.pushButton_2.clicked.connect(lambda: self.delete(group))
            QMessageBox.information(None, 'Успіх!', f'Групу {res} успішно видалено.')
    def back_menu(self,CurrentWindow,MainWindow):
        CurrentWindow.close()
        MainWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


