#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5 import  uic
from Lab.Lab_1 import Window1
from Lab.Lab_2 import Window2
from Lab.Lab_4 import Window4
from Lab.Lab_3 import Window3
from Lab.Lab_6 import Window6
#Этот модуль позволяет использовать многопоточность
import threading


#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("Main_window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class MaimWindow(QtWidgets.QMainWindow, ui):
    def __init__(self):
        #Объявляем расчётные классы

        #Инициализируем окно
        super().__init__()
        self.setupUi(self)
        # Прописываем действие на нажатие кнопки
        self.pushButton.clicked.connect(self.btnClicked1)
        self.pushButton_2.clicked.connect(self.btnClicked2)
        self.pushButton_3.clicked.connect(self.btnClicked3)
        self.pushButton_4.clicked.connect(self.btnClicked4)
        self.pushButton_5.clicked.connect(self.btnClicked)
        self.pushButton_6.clicked.connect(self.btnClicked6)

    # Этот метод описывает действи при нажатии кнопки2
    def btnClicked1(self):
        self.window1 = Window1.Window()  # Создаём объект класса
        self.window1.show()
        # Объявляем новый поток
        self.deman1 = threading.Thread(target=self.window1.show())
        # Запускаем новый поток
        self.deman1.start()


    #Этот метод описывает действи при нажатии кнопки2
    def btnClicked2(self):
        self.window2 = Window2.Window()  # Создаём объект класса
        self.window2.show()
        # Объявляем новый поток
        self.deman2 = threading.Thread(target=self.window2.show())
        # Запускаем новый поток
        self.deman2.start()

    # Этот метод описывает действи при нажатии кнопки4
    def btnClicked4(self):
        self.window4 = Window4.Window()  # Создаём объект класса
        self.window4.show()
        # Объявляем новый поток
        self.deman4 = threading.Thread(target=self.window4.show())
        # Запускаем новый поток
        self.deman4.start()

    # Этот метод описывает действи при нажатии кнопки3
    def btnClicked3(self):
        self.window3 = Window3.Window()  # Создаём объект класса
        self.window3.show()
        # Объявляем новый поток
        self.deman3 = threading.Thread(target=self.window3.show())
        # Запускаем новый поток
        self.deman3.start()

    #Этот метод описывает действи при нажатии кнопки6
    def btnClicked6(self):
        self.window6 = Window6.Window()  # Создаём объект класса
        self.window6.show()
        # Объявляем новый поток
        self.deman6 = threading.Thread(target=self.window6.show())
        # Запускаем новый поток
        self.deman6.start()

    #Заглушка Убрать при сборке
    def btnClicked(self):
        pass