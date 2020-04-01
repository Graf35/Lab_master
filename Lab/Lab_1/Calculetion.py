#Импортируем настройки конфигурации записи логирования
from Lab.Lab_1 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_1.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_1.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
from logging import info
from statistics import mean
import matplotlib.pyplot as plt
import math
from Sourse import Tab_1


#Применяем настройки логирования
logger=Log.Deman_log()
#Активируем возможность работы с файлами .doxc
Word=World()
#Делаем об этом запись в журнале.
info("Деман Word Призван!")


# Эта функция сохняет данные word
def save(parent):
    parent.label_2.setText("Введите ваши инициалы и фамилию")
    Name = dialog(parent)
    # Записываем имя автора работы
    Word.record({"Name": Name})
    # Делаем запись в журнале
    info("Начал записывать файл doxc")
    # Производим сохранение данных
    Word.save()
    # Делаем запись в журнале
    info("Закончил записывать файл doxc")
    parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_1")

class Lab_1():
    def __init__(self):
        # Делаем запись в журнале
        info("Начат расчёт лаботаторной работы 'Свободная конвекция'.")
        #Объявляем значение диаметра трубопровода модели
        self.d=0.04
        #Объявляем давление
        self.P1=1
        #Объявляем значение длинны модели трубопровода
        self.l=0.5
        #Объявляем температуры на поверхности паропровода
        self.ti=[95, 93, 90, 89, 88, 86, 83, 82, 81, 79]
        #Размеры участков паропровода
        self.li=[5, 15,  7, 13, 6, 14, 4, 16, 3, 17]
        #Диаметр паропровода
        self.D=200
        #Длинна паропровода
        self.L=100

    # Эта функция обрабатывает результаты первого опыта
    def experience_1 (self):
        #Напряжение на модели
        U=50
        # Ток на модели
        I=0.27
        # Температура в точках модели
        t=[47, 48, 49, 52, 54, 53, 51, 51, 49, 46]
        #площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp = mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"] + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        # Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        # безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu1 = a * self.d / (Tab_1("T", tcp, "Lamd") / 10 ** 2)
        # безразмерное число Рэлея
        self.Ra1 = Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)

    # Эта функция обрабатывает результаты второго опыта
    def experience_2 (self):
        # Напряжение на модели
        U=50
        # Ток на модели
        I=0.92
        # Температура в точках модели
        t=[94, 96, 99, 103, 106, 107, 101, 100, 98, 96]
        # площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp= mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"] + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        #Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        #безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu2= a * self.d / (Tab_1("T", tcp, "Lamd")/10**2)
        # безразмерное число Рэлея
        self.Ra2= Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)


    # Эта функция обрабатывает результаты третьего опыта
    def experience_3 (self):
        # Напряжение на модели
        U=50
        # Ток на модели
        I=2.58
        # Температура в точках модели
        t=[191, 194, 199, 203, 209, 208, 205, 201, 197, 193]
        # площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp = mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"]  + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        # Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        # безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu3 = a * self.d / (Tab_1("T", tcp, "Lamd") / 10 ** 2)
        # безразмерное число Рэлея
        self.Ra3 =Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)

    # Эта функция обрабатывает результаты четвертого опыта
    def experience_4 (self):
        # Напряжение на модели
        U=50
        # Ток на модели
        I=4.57
        # Температура в точках модели
        t=[288, 295, 298, 312, 314, 313, 306, 302, 282, 290]
        # площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp = mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"] + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        # Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        # безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu4 = a * self.d / (Tab_1("T", tcp, "Lamd") / 10 ** 2)
        # безразмерное число Рэлея
        self.Ra4 = Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)

    # Эта функция обрабатывает результаты пятого опыта
    def experience_5 (self):
        # Напряжение на модели
        U=50
        # Ток на модели
        I=6.88
        # Температура в точках модели
        t=[385, 390, 399, 408, 414, 415, 405, 402, 395, 387]
        # площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp = mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"] + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        # Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        # безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu5 = a * self.d / (Tab_1("T", tcp, "Lamd") / 10 ** 2)
        # безразмерное число Рэлея
        self.Ra5 = Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)

    # Эта функция обрабатывает результаты шестого опыта
    def experience_6 (self):
        # Напряжение на модели
        U=50
        # Ток на модели
        I=9.51
        # Температура в точках модели
        t=[483, 489, 499, 520, 519, 515, 508, 492, 490, 485]
        # площадь поверхности теплообмена
        F = math.pi * self.d * self.l
        # Средняя температура на поверхности модели
        tcp = mean(t)
        # Общая теплота
        Q = U * I
        # теплота, отведенная излучением
        Qi = 5.67 * 0.05 * abs(
            ((tcp + 273) / 100) ** 4 - ((self.sourse["tin"] + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk = Q - Qi
        # Коэфициент теплоотдачи
        a = (Tab_1("T", tcp, "Lamd"))/(Tab_1("T", tcp, "cp"))
        # безразмерное число Нуссельта (безразмерный коэффициент теплоотдачи)
        self.Nu6 = a * self.d / (Tab_1("T", tcp, "Lamd") / 10 ** 2)
        # безразмерное число Рэлея
        self.Ra6 = Tab_1("T", self.sourse["tin"], "Pr") * (
                    (9.81 * (1 / (self.sourse["tin"] + 273.15)) * abs(tcp - self.sourse["tin"]) * self.d ** 3) / (
                (Tab_1("T", self.sourse["tin"], "v") / 10 ** 6)) ** 2)

    #Эта функция обрабатывает реальный паропровод
    def steam(self):
        #Определяем коэфициент n
        n=mean(segmentation([math.log(self.Nu6), math.log(self.Nu5), math.log(self.Nu4), math.log(self.Nu3), math.log(self.Nu2), math.log(self.Nu1)],
                            [math.log(self.Ra1), math.log(self.Ra2), math.log(self.Ra3), math.log(self.Ra4), math.log(self.Ra5), math.log(self.Ra6)]))
        #Определяем коэфициент c
        c=self.Nu1/self.Ra6**n
        #Опредедяем площадь теплообмена паровровода
        F = math.pi * self.D * self.L
        # теплота, отведенная излучением
        Qi = 5.67 * self.sourse["stp"] * abs(
            ((mean(self.ti) + 273) / 100) ** 4 - ((self.sourse["tout"] - mean(self.ti) + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk =Tab_1("T", self.sourse["tout"], "a")*abs(mean(self.ti)-self.sourse["tout"])*F
        # Общая теплота
        Q = Qk + Qi

    def chart(self):
        x1=[math.log(self.Nu6),  math.log(self.Nu1)]
        y1 = [math.log(self.Ra1), mean([math.log(self.Ra1), math.log(self.Ra2),math.log(self.Ra3),math.log(self.Ra4),math.log(self.Ra5), math.log(self.Ra6)])]
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'Nu')
        ax.set_ylabel(u'Ra')
        # Добавляем заголовок графика
        ax.set_title(u'Логарифмическая зависимость Nu от Ra')
        # Рисуем линию конденсационного режима
        ax.plot(x1, y1, color='green', marker='o')
        ax.scatter([math.log(self.Nu5), math.log(self.Nu4), math.log(self.Nu3), math.log(self.Nu2),  math.log(self.Nu1)],
                   [math.log(self.Ra2),math.log(self.Ra3),math.log(self.Ra4),math.log(self.Ra5), math.log(self.Ra6)], marker='o', c='r', edgecolor='b')
        # Показываем график
        plt.show()