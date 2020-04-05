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
import seaborn as sns
import pandas as pd




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
        Word.record({"tc1": tcp, "lamd1":Tab_1("T", tcp, "Lamd"), "v1": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr1": round(Tab_1("T", self.sourse["tin"], "Pr")), "B1": round((1 / (self.sourse["tin"] + 273.15)),4),
                     "Q1": round(Q, 2), "Qk1": round(Qk, 2), "Qi1": round(Qi, 2), "a1": round(a, 2), "Ra1": round(self.Ra1, 2),
                     "Nu1": round(self.Nu1, 2)})

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
        Word.record({"tc2": tcp, "lamd2": Tab_1("T", tcp, "Lamd"), "v2": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr2": round(Tab_1("T", self.sourse["tin"], "Pr")),
                     "B2": round((1 / (self.sourse["tin"] + 273.15)), 4),
                     "Q2": round(Q, 2), "Qk2": round(Qk, 2), "Qi2": round(Qi, 2), "a2": round(a, 2),
                     "Ra2": round(self.Ra2, 2),
                     "Nu2": round(self.Nu2, 2)})


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
        Word.record({"tc3": tcp, "lamd3": Tab_1("T", tcp, "Lamd"), "v3": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr3": round(Tab_1("T", self.sourse["tin"], "Pr")),
                     "B3": round((1 / (self.sourse["tin"] + 273.15)), 4),
                     "Q3": round(Q, 2), "Qk3": round(Qk, 2), "Qi3": round(Qi, 2), "a3": round(a, 2),
                     "Ra3": round(self.Ra3, 2),
                     "Nu3": round(self.Nu3, 2)})

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
        Word.record({"tc4": tcp, "lamd4": Tab_1("T", tcp, "Lamd"), "v4": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr4": round(Tab_1("T", self.sourse["tin"], "Pr")),
                     "B4": round((1 / (self.sourse["tin"] + 273.15)), 4),
                     "Q4": round(Q, 2), "Qk4": round(Qk, 2), "Qi4": round(Qi, 2), "a4": round(a, 2),
                     "Ra4": round(self.Ra4, 2),
                     "Nu4": round(self.Nu4, 2)})

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
        Word.record({"tc5": tcp, "lamd5": Tab_1("T", tcp, "Lamd"), "v5": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr5": round(Tab_1("T", self.sourse["tin"], "Pr")),
                     "B5": round((1 / (self.sourse["tin"] + 273.15)), 4),
                     "Q5": round(Q, 2), "Qk5": round(Qk, 2), "Qi5": round(Qi, 2), "a5": round(a, 2),
                     "Ra5": round(self.Ra5, 2),
                     "Nu5": round(self.Nu5, 2)})

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
        Word.record({"tc6": tcp, "lamd6": Tab_1("T", tcp, "Lamd"), "v6": Tab_1("T", self.sourse["tin"], "v"),
                     "Pr6": round(Tab_1("T", self.sourse["tin"], "Pr")),
                     "B6": round((1 / (self.sourse["tin"] + 273.15)), 4),
                     "Q6": round(Q, 2), "Qk6": round(Qk, 2), "Qi6": round(Qi, 2), "a6": round(a, 2),
                     "Ra6": round(self.Ra6, 2),
                     "Nu6": round(self.Nu6, 2)})

    #Эта функция обрабатывает реальный паропровод
    def steam(self, parent):
        parent.Pixmap('Charts\Lab_1.png')
        parent.label_2.setText("По графику необходимо отпеделить координаты 2 точек, принадлежащих прямой \n Введите x1:")
        x1=float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих прямой \n Введите y1:")
        y1 =float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих прямой \n Введите x2:")
        x2 =float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих прямой \n Введите y2:")
        y2 =float(dialog(parent))
        #Определяем коэфициент n
        n=((y2-y1)/(x2-x1))
        #Определяем коэфициент c
        c=y1/x1**n
        #Опредедяем площадь теплообмена паровровода
        F = math.pi * self.D * self.L
        # теплота, отведенная излучением
        Qi = 5.67 * self.sourse["stp"] * abs(
            ((mean(self.ti) + 273) / 100) ** 4 - ((self.sourse["tout"] - mean(self.ti) + 273) / 100) ** 4) * F
        # теплота Q, отводимая от поверхности, Вт, отдается конвекцией
        Qk =Tab_1("T", self.sourse["tout"], "a")*abs(mean(self.ti)-self.sourse["tout"])*F
        # Общая теплота
        Q = Qk + Qi
        Word.record({"c": round(c, 2), "n": round(n, 2), "Qi": round(Qi, 2), "Qk": round(Qk, 2), "Q": round(Q, 2),})

    def chart(self, parent):
        parent.label_2.setText("Начал построение графика. Это может занять продолжительное время.")
        df = pd.DataFrame({
            "Nu": [math.log(self.Nu6), math.log(self.Nu5), math.log(self.Nu4), math.log(self.Nu3), math.log(self.Nu2), math.log(self.Nu1)],
            "Ra": [math.log(self.Ra1), math.log(self.Ra2), math.log(self.Ra3), math.log(self.Ra4), math.log(self.Ra5), math.log(self.Ra6)]})
        sns.set_style("whitegrid")
        gridobj = sns.lmplot(x="Ra", y="Nu", data=df, height=7, robust=True, palette='Set1', scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
        plt.savefig('Charts\Lab_1.png')

    # Эта функция сохняет данные word
    def save(self,parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        Word.record({"Name": Name, "Soursetin": self.sourse['tin'],"Soursetout": self.sourse['tout'], "Soursestp": self.sourse['stp']})
        # Делаем запись в журнале
        info("Начал записывать файл doxc")
        # Производим сохранение данных
        Word.save()
        # Делаем запись в журнале
        info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_1")

