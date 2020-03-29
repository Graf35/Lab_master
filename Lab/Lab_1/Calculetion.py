#Импортируем настройки конфигурации записи логирования
from Lab.Lab_1 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_1.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_1.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
import statistics
import numpy as np
import math


#Применяем настройки логирования
logger=Log.Deman_log()
#Активируем возможность работы с файлами .doxc
Word=World()
#Делаем об этом запись в журнале.
logging.info("Деман Word Призван!")


# Эта функция сохняет данные word
def save(parent):
    parent.label_2.setText("Введите ваши инициалы и фамилию")
    Name = dialog(parent)
    # Записываем имя автора работы
    Word.record({"Name": Name})
    # Делаем запись в журнале
    logging.info("Начал записывать файл doxc")
    # Производим сохранение данных
    Word.save()
    # Делаем запись в журнале
    logging.info("Закончил записывать файл doxc")
    parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_1")

class Lab_1():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Начат расчёт лаботаторной работы 'Свободная конвекция'.")
        self.d=40
        self.P1=1
        self.l=0.5
        self.ti={1:95, 2:93, 3: 90, 4:89, 5:88, 6:86, 7:83, 8:82, 9:81, 10:79}
        self.li={1:5, 2:15, 3: 7, 4:13, 5:6, 6:14, 7:4, 8:16, 9:3, 10:17}

    def experience_1 (self):
        U=50
        I=0.27
        t=[47, 48, 49, 52, 54, 53, 51, 51, 49, 46]
        F = math.pi * self.d * self.l
        tcp=statistics.mean(t)
        Qi=5.67*self.sourse['stp']*abs(((tcp+273)/100)**4-((self.sourse['tin']+273)/100)**4)*F
        Q=U*I
        Qk=Q-Qi
        alfa=Qk/(abs(tcp-self.sourse['tin'])*F)
        lamd=Q/(np.gradient(self.sourse['tin'])*F)
        Nu=alfa*self.d/lamd
        print(Nu, np.gradient(t))

