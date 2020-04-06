#Импортируем настройки конфигурации записи логирования
from Lab.Lab_6 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_6.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_6.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
import Sourse
import math
import matplotlib.pyplot as plt





#Применяем настройки логирования
logger=Log.Deman_log()
#Активируем возможность работы с файлами .doxc
Word=World()
#Делаем об этом запись в журнале.
logging.info("Деман Word Призван!")


# Эта функция сохняет данные word


class Lab_6():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Теплоотдача при конденсации чистого пара'.")
        self.a1 = []
        self.G1 = []
        self.a2 = []
        self.G2 = []
        self.a3 = []
        self.G3 = []
        self.a4 = []
        self.G4 = []
        self.dt1 = []
        self.dt2 = []


    def save(self,parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        Word.record({"Name": Name, "soursed12": self.sourse["d12"], "sourseH12": self.sourse["H12"], "soursed34": self.sourse["d34"]})
        # Делаем запись в журнале
        logging.info("Начал записывать файл doxc")
        # Производим сохранение данных
        Word.save()
        # Делаем запись в журнале
        logging.info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_6")


    def zadacha1(self):
        #0.1 MPa nado
        self.tc=[95, 85, 75, 65, 50, 40, 30, 20]
        # по таблице насыщенного пара
        for i in range(len(self.tc)):
            p = 1.013
            tn=99.62
            p1=0.958
            p2=0.598
            r=2256.8*10**3
            muj=11.97*10**6
            vj=20.02*10**6
            lya=2.37*10**(-2)
            Prj=1.08
            Ar=((9.81*self.sourse["H12"]**3)/vj**2)*(1-p2/p1)
            self.dt1.append(tn-self.tc[i])
            Z=(Ar**(1/3))*((lya*self.dt1[i])/(r*muj))
            if Z>=2300:
                Re=(89+0.024*(Prj/(Sourse.Tab_3("T", self.tc[i], "Pr")))**0.25*Prj**0.5*(Z-2300))**(4/3)
            else:
                Re=0.95*Z**0.78*(Prj/(Sourse.Tab_3("T", self.tc[i], "Pr")))**0.25
            self.a1.append(Re*r*muj/self.sourse["H12"]*self.dt1[i])
            F = math.pi*self.sourse["d12"]*self.sourse["H12"]
            self.G1.append(3600*self.a1[i]*self.dt1[i]*F)
        Word.record({"a10": round(self.a1[0], 2), "a11": round(self.a1[1], 2), "a12": round(self.a1[2], 2), "a13": round(self.a1[3], 2),
                     "a14": round(self.a1[4], 2), "a15": round(self.a1[4], 2), "a16": round(self.a1[6], 2), "a17": round(self.a1[0], 2),
                     "G10": round(self.G1[0], 2), "G11": round(self.G1[1], 2), "G12": round(self.G1[2], 2), "G13": round(self.G1[3], 2),
                      "G14": round(self.G1[4], 2), "G15": round(self.G1[5], 2), "G16": round(self.G1[6], 2), "G17": round(self.G1[7], 2)})

    def zadacha2(self):
        # по таблице насыщенного пара
        for i in range(len(self.tc)):
            p = 1.013
            tn=99.62
            p1=0.9589
            p2=0.598
            r = 2256.8 * 10 ** 3
            muj = 11.97 * 10 ** 6
            vj = 20.02 * 10 ** 6
            lya = 2.37 * 10 ** (-2)
            Prj=1.08
            po=(Sourse.Tab_3("T", self.tc[i], "p"))
            Ar=((9.81*self.sourse["H12"]**3)/vj**2)*(1-p2/p1)
            self.dt2.append(tn-self.tc[i])
            Z=(Ar**(1/3))*((lya*self.dt2[i])/(r*muj))
            if Z>=2300:
                Re=(89+0.024*(Prj/(Sourse.Tab_3("T", self.tc[i], "Pr")))**0.25*Prj**0.5*(Z-2300))**(4/3)
            else:
                Re=0.95*Z**0.78*(Prj/(Sourse.Tab_3("T", self.tc[i], "Pr")))**0.25
            self.a2.append(0.728*((lya**3*po**2*9.81*r)/muj*(tn-self.tc[i])*self.sourse["d12"])**(1/4))
            F = math.pi*self.sourse["d12"]*self.sourse["H12"]
            self.G2.append(3600*self.a2[i]*self.dt2[i]*F)
        Word.record({"a20": round(self.a2[0], 2), "a21": round(self.a2[1], 2), "a22": round(self.a2[2], 2),
                     "a23": round(self.a2[3], 2),
                     "a24": round(self.a2[4], 2), "a25": round(self.a2[4], 2), "a26": round(self.a2[6], 2),
                     "a27": round(self.a2[0], 2),
                     "G20": round(self.G2[0], 2), "G21": round(self.G2[1], 2), "G22": round(self.G2[2], 2),
                     "G23": round(self.G2[3], 2),
                     "G24": round(self.G2[4], 2), "G25": round(self.G2[5], 2), "G26": round(self.G2[6], 2),
                     "G27": round(self.G2[7], 2)})

    def chart(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't')
        ax.set_ylabel(u'a')
        # Добавляем заголовок графика
        ax.set_title(u'α=f(∆t)')
        # Рисуем линию конденсационного режима
        ax.plot(self.dt1, self.a1, label=u'задача 1', color='green', marker='o')
        ax.plot(self.dt2, self.a2,  label=u'задача 2', color='black', marker='o')
        # Показываем график
        plt.legend()
        plt.savefig("Charts\graf1.png")


    def chart2(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't')
        ax.set_ylabel(u'g')
        # Добавляем заголовок графика
        ax.set_title(u'G =f(∆t)')
        # Рисуем линию конденсационного режима
        ax.plot(self.dt1, self.G1, label=u'задача 1', color ='orange', marker='o')
        ax.plot(self.dt2, self.G2,  label=u'задача 2', color='red', marker='o')
        # Показываем график
        plt.legend()
        plt.savefig("Charts\graf2.png")

    def zadacha3(self):
        self.h=[0.2, 0.4, 0.6, 0.8, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4]
        for i in range(len(self.h)):
            tc=270
            p=64.19
            #bar esli nado to 6,41 MPa
            tn = 275.56
            p1 = 30.84
            p2 = 28.09
            r = 1604.4*10**3
            muj =19.32*10**6
            vj =0.688*10**6
            lya =5.10*10**(-2)
            Prj =0.88
            Ar = ((9.81 *self.h[i] ** 3) / vj ** 2) * (1 - p2 / p1)
            dt = tn - tc
            Z = (Ar ** (1 / 3)) * ((lya * dt) / (r * muj))
            if Z >= 2300:
                Re = (89 + 0.024 * (Prj / (Sourse.Tab_3("T", tc, "Pr"))) ** 0.25 * Prj ** 0.5 * (Z - 2300)) ** (
                            4 / 3)
            else:
                Re = 0.95 * Z ** 0.78 * (Prj / (Sourse.Tab_3("T", tc, "Pr"))) ** 0.25
            self.a3.append(Re * r * muj / self.h[i] * dt)
            F = math.pi * self.sourse["d34"] * self.h[i]
            self.G3.append(3600 * self.a3[i] * dt * F)
        Word.record({"a30": round(self.a3[0], 2), "a31": round(self.a3[1], 2), "a32": round(self.a3[2], 2),
                     "a33": round(self.a3[3], 2),
                     "a34": round(self.a3[4], 2), "a35": round(self.a3[4], 2), "a36": round(self.a3[6], 2),
                     "a37": round(self.a3[7], 2), "a38": round(self.a3[8], 2), "a39": round(self.a3[9], 2),
                     "a310": round(self.a3[10], 2), "a311": round(self.a3[11], 2),
                     "G30": round(self.G3[0], 2), "G31": round(self.G3[1], 2), "G32": round(self.G3[2], 2),
                     "G33": round(self.G3[3], 2),
                     "G34": round(self.G3[4], 2), "G35": round(self.G3[5], 2), "G36": round(self.G3[6], 2),
                     "G37": round(self.G3[7], 2), "G38": round(self.G3[8], 2), "G39": round(self.G3[9], 2),
                     "G310": round(self.G3[10], 2), "G311": round(self.G3[11], 2)})

    def zadacha4(self):
        for i in range(len(self.h)):
            tc = 270
            p = 64.19
            # bar esli nado to 6,41 MPa
            tn = 275.56
            p1 = 30.84
            p2 = 28.09
            r = 1604.4 * 10 ** 3
            muj = 19.32 * 10 ** 6
            vj = 0.688 * 10 ** 6
            lya = 5.10 * 10 ** (-2)
            Prj = 0.88
            po=(Sourse.Tab_3("T", tc, "p"))
            Ar = ((9.81 * self.h[i] ** 3) / vj ** 2) * (1 - p2 / p1)
            dt = tn - tc
            Z = (Ar ** (1 / 3)) * ((lya * dt) / (r * muj))
            if Z >= 2300:
                Re = (89 + 0.024 * (Prj / (Sourse.Tab_3("T", tc, "Pr"))) ** 0.25 * Prj ** 0.5 * (Z - 2300)) ** (
                        4 / 3)
            else:
                Re = 0.95 * Z ** 0.78 * (Prj / (Sourse.Tab_3("T", tc, "Pr"))) ** 0.25
            self.a4.append(0.728*((lya**3*po**2*9.81*r)/muj*(tn-tc)*self.sourse["d34"])**(1/4))
            F = math.pi * self.sourse["d34"] * self.h[i]
            self.G4.append(3600 * self.a4[i] * dt * F)
        Word.record({"a40": round(self.a4[0], 2), "a41": round(self.a4[1], 2), "a42": round(self.a4[2], 2),
                     "a43": round(self.a4[3], 2),
                     "a44": round(self.a3[4], 2), "a45": round(self.a4[4], 2), "a46": round(self.a4[6], 2),
                     "a47": round(self.a4[7], 2), "a48": round(self.a4[8], 2), "a49": round(self.a4[9], 2),
                     "a410": round(self.a4[10], 2), "a411": round(self.a4[11], 2),
                     "G40": round(self.G4[0], 2), "G41": round(self.G4[1], 2), "G42": round(self.G4[2], 2),
                     "G43": round(self.G4[3], 2),
                     "G44": round(self.G4[4], 2), "G45": round(self.G4[5], 2), "G46": round(self.G4[6], 2),
                     "G47": round(self.G4[7], 2), "G48": round(self.G4[8], 2), "G49": round(self.G4[9], 2),
                     "G410": round(self.G4[10], 2), "G411": round(self.G4[11], 2)})


    def chart3(self):
         # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'h')
        ax.set_ylabel(u'a')
         # Добавляем заголовок графика
        ax.set_title(u'α=f(h)')
        # Рисуем линию конденсационного режима
        ax.plot(self.h, self.a3, label=u'задача 3', color='green', marker='o')
        ax.plot(self.h, self.a4, label=u'задача 4', color='black', marker='o')
        # Показываем график
        plt.legend()
        plt.savefig("Charts\graf3.png")

    def chart4(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'h')
        ax.set_ylabel(u'g')
        # Добавляем заголовок графика
        ax.set_title(u'G =f(∆h)')
        # Рисуем линию конденсационного режима
        ax.plot(self.h, self.G3, label=u'задача 3', color='orange', marker='o')
        ax.plot(self.h, self.G4, label=u'задача 4', color='red', marker='o')
        # Показываем график
        plt.legend()
        plt.savefig("Charts\graf4.png")
