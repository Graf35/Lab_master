#Импортируем настройки конфигурации записи логирования
from Lab.Lab_2 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_2.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_2.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
import pandas as pd
import math
import matplotlib.pyplot as plt
import Sourse
import seaborn as sns
from statistics import mean



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
    parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_2")

class Lab_2():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Моделирование теплообмена в коридорном пучке'.")
        self.d = 0.01
        self.l = 0.5
        self.s1 = 1.5 * self.d
        self.s2 = 2 * self.d
        self.e = 0.8
        self.Nuvoz=[]
        self.Revoz=[]
        self.Nuvod=[]
        self.Revod=[]
        self.Nuoil=[]
        self.Reoil=[]
    def vozduh(self):
        Qi=[]
        Qk=[]
        a=[]
        tc = [66.1, 62.1, 58.1, 54.1, 50.1, 46.1, 42.1, 38.1, 34.1, 30.1, 26.1, 22.1]
        w = [2, 3, 4, 5, 6, 7, 8, 10, 20, 30, 50, 100]
        for i in range (len(tc)):
            U=220
            I=0.15
            Q = U * I
            F = math.pi * self.d * self.l
            Qi.append(5.67*self.e*abs(((tc[i]+273)/100)**4-((self.sourse["tvoz"]+273)/100)**4)*F)
            Qk.append(Q - Qi[i])
            a.append(Qk[i]/abs(tc[i]-self.sourse["tvoz"])*F)
            self.Nuvoz.append(math.log((a[i]*self.d)/(Sourse.Tab_1("T", self.sourse[
            "tvoz"], "Lamd") / 10 ** 2)))
            self.Revoz.append(math.log(w[i]*self.d/(Sourse.Tab_1("T", self.sourse[
            "tvoz"], "v") / 10 ** 6)))
        Word.record({"Qvoz": round(Q, 2), "Qivoz1": round(Qi[0], 2), "Qivoz2": round(Qi[1], 2), "Qivoz3": round(Qi[2], 2),
                     "Qivoz4": round(Qi[3], 2), "Qivoz5": round(Qi[4], 2), "Qivoz6": round(Qi[5], 2),
                     "Qivoz7": round(Qi[6], 2), "Qivoz8": round(Qi[7], 2), "Qivoz9": round(Qi[8], 2),
                     "Qivoz10": round(Qi[9], 2), "Qivoz11": round(Qi[10], 2), "Qivoz12": round(Qi[11], 2), "Qkvoz1": round(Qk[0], 2), "Qkvoz2": round(Qk[1], 2), "Qkvoz3": round(Qk[2], 2),
                     "Qkvoz4": round(Qk[3], 2), "Qkvoz5": round(Qk[4], 2), "Qkvoz6": round(Qk[5], 2),
                     "Qkvoz7": round(Qk[6], 2), "Qkvoz8": round(Qk[7], 2), "Qkvoz9": round(Qk[8], 2),
                     "Qkvoz10": round(Qk[9], 2), "Qkvoz11": round(Qk[10], 2), "Qkvoz12": round(Qk[11], 2),
                     "avoz1": round(a[0], 2), "avoz2": round(a[1], 2), "avoz3": round(a[2], 2),
                     "avoz4": round(a[3], 2), "avoz5": round(a[4], 2), "avoz6": round(a[5], 2),
                     "avoz7": round(a[6], 2), "avoz8": round(a[7], 2), "avoz9": round(a[8], 2),
                     "avoz10": round(a[9], 2), "avoz11": round(a[10], 2), "avoz12": round(a[11], 2),
                     "Revoz1": round(self.Revoz[0], 2), "Revoz2": round(self.Revoz[1], 2), "Revoz3": round(self.Revoz[2], 2),
                     "Revoz4": round(self.Revoz[3], 2), "Revoz5": round(self.Revoz[4], 2), "Revoz6": round(self.Revoz[5], 2),
                     "Revoz7": round(self.Revoz[6], 2), "Revoz8": round(self.Revoz[7], 2), "Revoz9": round(self.Revoz[8], 2),
                     "Revoz10": round(self.Revoz[9], 2), "Revoz11": round(self.Revoz[10], 2), "Revoz12": round(self.Revoz[11], 2),
                     "Nuvoz1": round(self.Nuvoz[0], 2), "Nuvoz2": round(self.Nuvoz[1], 2), "Nuvoz3": round(self.Nuvoz[2], 2),
                     "Nuvoz4": round(self.Nuvoz[3], 2), "Nuvoz5": round(self.Nuvoz[4], 2), "Nuvoz6": round(self.Nuvoz[5], 2),
                     "Nuvoz7": round(self.Nuvoz[6], 2), "Nuvoz8": round(self.Nuvoz[7], 2), "Nuvoz9": round(self.Nuvoz[8], 2),
                     "Nuvoz10": round(self.Nuvoz[9], 2), "Nuvoz11": round(self.Nuvoz[10], 2), "Nuvoz12": round(self.Nuvoz[11], 2),
                     "lamdvoz": (Sourse.Tab_1("T", self.sourse["tvoz"], "Lamd")), "vvoz": (Sourse.Tab_1("T", self.sourse["tvoz"], "v")),
                     "Prvoz": round(Sourse.Tab_1("T", self.sourse["tvoz"], "Pr"))
                     })

    def voda(self):
        a = []
        tc = [75.1, 70.1, 65.1, 60.1, 55.1, 50.1, 45.1, 40.1, 35.1, 30.1, 25.1, 20.1]
        w = [0.1, 0.2, 0.5, 0.8, 1, 1.5, 2, 3, 5, 10, 12, 15]
        for i in range(len(tc)):
            U = 220
            I = 10
            F = math.pi * self.d * self.l
            Qi=0
            Q = U * I
            Qk = Q - Qi
            a.append( Qk / abs(tc[i] - self.sourse["tvod"]) * F)
            self.Nuvod.append(math.log((a[i] * self.d) / (Sourse.Tab_3("T", self.sourse[
            "tvod"], "lamd") / 10 ** 2)))
            self.Revod.append(math.log(w[i] * self.d / (Sourse.Tab_3("T", self.sourse[
            "tvod"], "v") / 10 ** 6)))
        Word.record({"Qvod": round(Q, 2), "Qivod": round(Qi, 2),
                     "avod1": round(a[0], 2), "avod2": round(a[1], 2), "avod3": round(a[2], 2),
                     "avod4": round(a[3], 2), "avod5": round(a[4], 2), "avod6": round(a[5], 2),
                     "avod7": round(a[6], 2), "avod8": round(a[7], 2), "avod9": round(a[8], 2),
                     "avod10": round(a[9], 2), "avod11": round(a[10], 2), "avod12": round(a[11], 2),
                     "Revod1": round(self.Revoz[0], 2), "Revod2": round(self.Revoz[1], 2), "Revod3": round(self.Revoz[2], 2),
                     "Revod4": round(self.Revoz[3], 2), "Revod5": round(self.Revoz[4], 2), "Revod6": round(self.Revoz[5], 2),
                     "Revod7": round(self.Revoz[6], 2), "Revod8": round(self.Revoz[7], 2), "Revod9": round(self.Revoz[8], 2),
                     "Revod10": round(self.Revoz[9], 2), "Revod11": round(self.Revoz[10], 2), "Revod12": round(self.Revoz[11], 2),
                     "Nuvod1": round(self.Nuvoz[0], 2), "Nuvod2": round(self.Nuvoz[1], 2), "Nuvod3": round(self.Nuvoz[2], 2),
                     "Nuvod4": round(self.Nuvoz[3], 2), "Nuvod5": round(self.Nuvoz[4], 2), "Nuvod6": round(self.Nuvoz[5], 2),
                     "Nuvod7": round(self.Nuvoz[6], 2), "Nuvod8": round(self.Nuvoz[7], 2), "Nuvod9": round(self.Nuvoz[8], 2),
                     "Nuvod10": round(self.Nuvoz[9], 2), "Nuvod11": round(self.Nuvoz[10], 2), "Nuvod12": round(self.Nuvoz[11], 2),
                     "lamdvod": (Sourse.Tab_3("T", self.sourse["tvoz"], "lamd")), "vvod": (Sourse.Tab_3("T", self.sourse["tvoz"], "v")),
                     "Prvod": round(Sourse.Tab_3("T", self.sourse["tvoz"], "Pr"))
                     })

    def oil(self):
        a=[]
        tc = [150, 147, 145, 143, 141, 139, 137, 135, 133, 131, 129, 127]
        w = [0.7, 1, 1.5, 2, 3, 5, 8, 10, 15, 20, 25, 30]
        for i in range(len(tc)):
            U = 220
            I = 3
            F = math.pi * self.d * self.l
            Qi = 0
            Q = U * I
            Qk = Q - Qi
            a.append( Qk / abs(tc[i] - self.sourse["toil"]) * F)
            self.Nuoil.append(math.log((a[i] * self.d) / (Sourse.Tab_8("T", self.sourse[
            "toil"], "lamd") / 10 ** 2)))
            self.Reoil.append(math.log(w[i] * self.d / (Sourse.Tab_8("T", self.sourse[
            "toil"], "v") / 10 ** 6)))
        Word.record({"Qoil": round(Q, 2), "Qioil": round(Qi, 2),
                     "aoil1": round(a[0], 2), "aoil2": round(a[1], 2), "aoil3": round(a[2], 2),
                     "aoil4": round(a[3], 2), "aoil5": round(a[4], 2), "aoil6": round(a[5], 2),
                     "aoil7": round(a[6], 2), "aoil8": round(a[7], 2), "aoil9": round(a[8], 2),
                     "aoil10": round(a[9], 2), "aoil11": round(a[10], 2), "aoil12": round(a[11], 2),
                     "Reoil1": round(self.Revoz[0], 2), "Reoil2": round(self.Revoz[1], 2), "Reoil3": round(self.Revoz[2], 2),
                     "Reoil4": round(self.Revoz[3], 2), "Reoil5": round(self.Revoz[4], 2), "Reoil6": round(self.Revoz[5], 2),
                     "Reoil7": round(self.Revoz[6], 2), "Reoil8": round(self.Revoz[7], 2), "Reoil9": round(self.Revoz[8], 2),
                     "Reoil10": round(self.Revoz[9], 2), "Reoil11": round(self.Revoz[10], 2), "Reoil12": round(self.Revoz[11], 2),
                     "Nuoil1": round(self.Nuvoz[0], 2), "Nuoil2": round(self.Nuvoz[1], 2), "Nuoil3": round(self.Nuvoz[2], 2),
                     "Nuoil4": round(self.Nuvoz[3], 2), "Nuoil5": round(self.Nuvoz[4], 2), "Nuoil6": round(self.Nuvoz[5], 2),
                     "Nuoil7": round(self.Nuvoz[6], 2), "Nuoil8": round(self.Nuvoz[7], 2), "Nuoil9": round(self.Nuvoz[8], 2),
                     "Nuoil10": round(self.Nuvoz[9], 2), "Nuoil11": round(self.Nuvoz[10], 2), "Nuoil12": round(self.Nuvoz[11], 2),
                     "lamdoil": (Sourse.Tab_8("T", self.sourse["tvoz"], "lamd")), "voil": (Sourse.Tab_8("T", self.sourse["tvoz"], "v")),
                     "Proil": round(Sourse.Tab_8("T", self.sourse["tvoz"], "Pr"))
                     })

    def general(self, parent):
        parent.Pixmap('Charts\Lab_2_general.png')
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих зеленой прямой. \n Введите x1:")
        x1 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих зеленой прямой \n Введите y1:")
        y1 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих зеленой прямой \n Введите x2:")
        x2 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих зеленой прямой \n Введите y2:")
        y2 = float(dialog(parent))
        #Определяем коэфициент n
        self.n=((y2-y1)/(x2-x1))


    def gen(self, parent):
        parent.Pixmap('Charts\Lab_2.png')
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих синей прямой. \n Введите x1:")
        x1 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих синей прямой \n Введите y1:")
        y1 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих синей прямой \n Введите x2:")
        x2 = float(dialog(parent))
        parent.label_2.setText(
            "По графику необходимо отпеделить координаты 2 точек, принадлежащих синей прямой \n Введите y2:")
        y2 = float(dialog(parent))
        # Определяем коэфициент d
        d = ((y2 - y1) / (x2 - x1))
        # Определяем коэфициент c
        c=self.Nuoil[0]/(self.Reoil[0]**self.n*((Sourse.Tab_8("T", self.sourse["toil"], "v")) / 10 ** 6)**d)
        Word.record({"c": round(c, 2), "d": round(d, 2), "n": round(self.n, 2)})

    def chart(self, parent):
        parent.label_2.setText("Собираю данные")
        self.df = pd.DataFrame({
            "Nu": pd.Series([self.Nuvod[0], self.Nuvod[1], self.Nuvod[2],self.Nuvod[3],self.Nuvod[4],self.Nuvod[5],self.Nuvod[6],
                             self.Nuvod[7],self.Nuvod[8],self.Nuvod[9],self.Nuvod[10],self.Nuvod[11], self.Nuvoz[0],self.Nuvoz[1],
                             self.Nuvoz[2],self.Nuvoz[3],self.Nuvoz[4],self.Nuvoz[5],self.Nuvoz[6],self.Nuvoz[7],self.Nuvoz[8],
                             self.Nuvoz[9],self.Nuvoz[10],self.Nuvoz[11], self.Nuoil[0],self.Nuoil[1], self.Nuoil[2], self.Nuoil[3],
                             self.Nuoil[4], self.Nuoil[5], self.Nuoil[6], self.Nuoil[7], self.Nuoil[8], self.Nuoil[9], self.Nuoil[10],
                             self.Nuoil[11]]),
            "Re": pd.Series([self.Revod[0], self.Revod[1],self.Revod[2],self.Revod[3],self.Revod[4],self.Revod[5],self.Revod[6],
                             self.Revod[7],self.Revod[8],self.Revod[9],self.Revod[10],self.Revod[11], self.Revoz[0], self.Revoz[1],
                             self.Revoz[2],self.Revoz[3],self.Revoz[4],self.Revoz[5],self.Revoz[6],self.Revoz[7],self.Revoz[8],
                             self.Revoz[9],self.Revoz[10],self.Revoz[11], self.Reoil[0],  self.Reoil[1], self.Reoil[2], self.Reoil[3],
                             self.Reoil[4], self.Reoil[5], self.Reoil[6], self.Reoil[7], self.Reoil[8], self.Reoil[9], self.Reoil[10],
                             self.Reoil[11]]),
            "cyl": pd.Series(["vod","vod","vod","vod","vod","vod","vod","vod","vod","vod","vod","vod", "voz",
                                                     "voz","voz","voz","voz","voz","voz","voz","voz","voz","voz","voz","oil",
                                                     "oil","oil","oil","oil","oil","oil","oil","oil","oil","oil","oil"])
        })
        parent.label_2.setText("Строю график. Это может занять продолжительное время")
        df_select = self.df.loc[self.df.cyl.isin(["vod", "voz", "oil"]), :]
        sns.set_style("whitegrid")
        gridobj = sns.lmplot(x="Re", y="Nu", data=df_select, hue="cyl",
                     height=7, aspect=1.6, robust=True, palette='tab10',
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
        # Сохраняем график
        plt.savefig("Charts\Lab_2_general.png")

    def chart2(self, parent):
        df = pd.DataFrame({
            "Nu/Re": pd.Series([self.Nuoil[0]/self.Reoil[0]**self.n, self.Nuvod[0]/self.Revod[0]**self.n, self.Nuvoz[0]/self.Revoz[0]**self.n]),
            "Pr": pd.Series([ (Sourse.Tab_8("T", self.sourse["toil"], "Pr")), (Sourse.Tab_3("T", self.sourse["tvod"], "Pr")), (Sourse.Tab_1("T", self.sourse["tvoz"], "Pr"))]),
            "cyl": pd.Series(["oil", "vod","voz"])
        })
        parent.label_2.setText("Строю график. Это может занять продолжительное время")
        sns.set_style("whitegrid")
        gridobj = sns.lmplot(x="Nu/Re", y="Pr", data=df,
                     height=7, aspect=1.6, robust=True, palette='tab10',
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
        # Сохраняем график
        plt.savefig("Charts\Lab_2.png")

    # Эта функция сохняет данные word
    def save(self, parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        Word.record({"Name": Name, "Soursetvoz": self.sourse["tvoz"], "Soursetvod": self.sourse["tvod"], "Soursetoil": self.sourse["toil"]})
        # Делаем запись в журнале
        logging.info("Начал записывать файл doxc")
        # Производим сохранение данных
        Word.save()
        # Делаем запись в журнале
        logging.info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_2")