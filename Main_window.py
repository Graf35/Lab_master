#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5 import  uic
from Lab.Lab_1 import Window1
from Lab.Lab_2 import Window2
from Lab.Lab_6 import Window6


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
        self.pushButton_3.clicked.connect(self.btnClicked)
        self.pushButton_4.clicked.connect(self.btnClicked)
        self.pushButton_5.clicked.connect(self.btnClicked)
        self.pushButton_6.clicked.connect(self.btnClicked6)

    # Этот метод описывает действи при нажатии кнопки2
    def btnClicked1(self):
        self.window = Window1.Window()  # Создаём объект класса
        self.window.show()

    #Этот метод описывает действи при нажатии кнопки2
    def btnClicked2(self):
        self.window = Window2.Window()  # Создаём объект класса
        self.window.show()

    #Этот метод описывает действи при нажатии кнопки2
    def btnClicked6(self):
        self.window = Window6.Window()  # Создаём объект класса
        self.window.show()

    #Заглушка Убрать при сборке
    def btnClicked(self):
        pass