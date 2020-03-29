#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import  uic


#Этот модуль позволяет использовать многопоточность
import threading

#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("Window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class Window(QtWidgets.QMainWindow, ui):
    def __init__(self):
        #Объявляем расчётные классы

        #Инициализируем окно
        super().__init__()
        self.setupUi(self)
        #Прописываем действие на открытие меню
        self.action.triggered.connect(self.sourse)
        #Выводим сообщение пользователю
        self.label_2.setText("Выберите файл начальных данных")
        #Прописываем действие на нажатие кнопки
        self.pushButton.clicked.connect(self.btnClicked)
        #Устанавливаем стандартную картинку
        self.Pixmap("Windows\MainWindow.jpg")


    #Этот метод позволяет устанавливать другое изображение на экран
    def Pixmap(self, way):
        #Разбиваем на пиксили изображение
        pixmap = QPixmap(way)
        #Вставляем это изображение на экран
        self.label.setPixmap(pixmap)

    #Этот метод описывает действи при нажатии кнопки
    def btnClicked(self):
        #Записываем введенное значение в переменную
        self.inpat=self.lineEdit_2.text()
        #Очищаем поле
        self.lineEdit_2.clear()

    #Этот метод описывает процесс выбора файла с исходными данными
    def sourse(self):
        #Определяем путь до файла
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/sourse')[0]
        #Сообщаем значения его переменных в классы
        #self.cycle.sourse=entry(fname)
        #Сообщаем путь к файлу в классы
        self.cycle.fname=fname
        #Объявляем новый поток
        self.deman = threading.Thread(target=self.prog)
        #Запускаем новый поток
        self.deman.start()







