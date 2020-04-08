#Импортируем настройки конфигурации записи логирования
from Lab.Lab_4 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_4.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_4.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
from Sourse import Tab_3
from math import pi, exp
#Импортируем модуль Window. Он необходим для возможности работы с оконным интерфейсом.
import matplotlib.pyplot as plt



#Применяем настройки логирования
logger=Log.Deman_log()
#Активируем возможность работы с файлами .doxc
Word=World()
#Делаем об этом запись в журнале.
logging.info("Деман Word Призван!")


class Lab_4():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Начат расчёт лаботаторной работы 'Свободная конвекция'.")
        self.n1=5
        self.n2=10
        self.n=[1, 2, 5, 10, 20, 50, 100]
        self.G1=[500, 1000, 2000, 5000, 10000, 50000]
        self.G2=[2000, 3000, 5000, 10000, 20000, 50000]
        self.d1=32
        self.d2=35
        self.D=48
        self.l=1.75


    def cal2(self):
        w2=[]
        Re2=[]
        Nu2=[]
        a2=[]
        k=[]
        C2=[]
        f=[]
        dt1=[]
        dt2=[]
        self.tg12=[]
        self.tg22 = []
        self.Q2=[]
        for i in range(len(self.G2)):
            w1=(4*self.sourse['Gvx'])/(Tab_3("T", self.sourse['tvx'], "p")* pi*self.d1**2*3600)
            w2.append((4 * self.G2[i]) / (Tab_3("T", self.sourse['tn'], "p") * pi * (self.D**2-self.d1 ** 2) * 3600))
            Re1=w1*self.d1/(Tab_3("T", self.sourse['tvx'], "v"))
            Nu1=0.021*Re1**0.8*(Tab_3("T", self.sourse['tvx'], "Pr"))**0.43*((Tab_3("T", self.sourse['tvx'], "Pr"))/(Tab_3("T", (0.5*(self.sourse['tvx']+self.sourse['tn'])), "Pr")))**0.25
            a1=Nu1*(Tab_3("T", self.sourse['tvx'], "lamd"))/self.d1
            Re2.append(w2[i] * (self.D-self.d2) / (Tab_3("T", self.sourse['tn'], "v")))
            Nu2.append(0.021 * Re2[i] ** 0.8 * (Tab_3("T", self.sourse['tn'], "Pr")) ** 0.43 * (
                    (Tab_3("T", self.sourse['tn'], "Pr")) / (
                Tab_3("T", (0.5 * (self.sourse['tvx'] + self.sourse['tn'])), "Pr"))) ** 0.25)
            a2.append( Nu2[i] * (Tab_3("T", self.sourse['tn'], "lamd")) / self.d2)
            k.append(1/(1/a1+((self.d2-self.d1)/2)/(Tab_3("T", (0.5*(self.sourse['tvx']+self.sourse['tn'])), "lamd"))+1/a2[i]))
            F=self.n2*pi*self.l*((self.d1+self.d2)/2)
            C1=self.sourse['Gvx']*(Tab_3("T", self.sourse['tvx'], "cp"))
            C2.append(self.G2[i] * (Tab_3("T", self.sourse['tn'], "cp")))
            f.append((1-exp(k[i]*F/C1*(1-(C1/C2[i]))))/(1-(C1/C2[i])* exp(-k[i]*F/C1*(1-(C1/C2[i])))))
            dt1.append((self.sourse['tvx']-self.sourse['tn'])*f[i])
            dt2.append(dt1[i]*C1/C2[i])
            self.tg12.append(self.sourse['tvx']-dt1[i])
            self.tg22.append(self.sourse['tn'] - dt2[i])
            self.Q2.append(C1*dt1[i])
        Word.record({"ww1": round(w1 * 10 ** 6, 2), "Re12": round(Re1 * 10 ** 6, 2), "Nu12": round(Nu1 * 10 ** 6, 2),
                     "a12": round(a1 * 10 ** 6, 2), "F2": round(F, 2), "C12": round(C1, 2),
                     "ww10": round(w2[0]*10**6, 2), "ww11": round(w2[1]*10**6, 2), "ww12": round(w2[2]*10**6, 2), "ww13": round(w2[3]*10**6, 2), "ww14": round(w2[4]*10**6, 2), "ww15": round(w2[5]*10**6, 2),
                     "rRe10": round(Re2[0]*10**6, 2), "rRe11": round(Re2[1]*10**6, 2), "rRe12": round(Re2[2]*10**6, 2), "rRe13": round(Re2[3]*10**6, 2), "rRe14": round(Re2[4]*10**6, 2), "rRe15": round(Re2[5]*10**6, 2),
                     "nNu10": round(Nu2[0]*10**6, 2), "nNu11": round(Nu2[1]*10**6, 2), "nNu12": round(Nu2[2]*10**6, 2), "nNu13": round(Nu2[3]*10**6, 2), "nNu14": round(Nu2[4]*10**6, 2), "nNu15": round(Nu2[5]*10**6, 2),
                     "aa10": round(a2[0]*10**6, 2), "aa11": round(a2[1]*10**6, 2), "aa12": round(a2[2]*10**6, 2), "aa13": round(a2[3]*10**6, 2), "aa14": round(a2[4]*10**6, 2), "aa15": round(a2[5]*10**6, 2),
                     "kk10": round(k[0]*10**6, 2), "kk11": round(k[1]*10**6, 2), "kk12": round(k[2]*10**6, 2), "kk13": round(k[3]*10**6, 2), "kk14": round(k[4]*10**6, 2), "kk15": round(k[5]*10**6, 2),
                     "cC10": round(C2[0], 2), "cC11": round(C2[1], 2), "cC12": round(C2[2], 2), "cC13": round(C2[3], 2), "cC14": round(C2[4], 2), "cC15": round(C2[5], 2),
                     "ddt10": round(dt1[0]*10**4, 2), "ddt11": round(dt1[1]*10**4, 2), "ddt12": round(dt1[2]*10**4, 2), "ddt13": round(dt1[3]*10**4, 2), "ddt14": round(dt1[4]*10**4, 2), "ddt15": round(dt1[5]*10**4, 2),
                     "ddt20": round(dt2[0]*10**4, 2), "ddt21": round(dt2[1]*10**4, 2), "ddt22": round(dt2[2]*10**4, 2), "ddt23": round(dt2[3]*10**4, 2), "ddt24": round(dt2[4]*10**4, 2), "ddt25": round(dt2[5]*10**4, 2),
                     "ttg10": round(self.tg11[0], 2), "ttg11": round(self.tg11[1], 2), "ttg12": round(self.tg11[2], 2),
                     "ttg13": round(self.tg11[3], 2), "ttg14": round(self.tg11[4], 2), "ttg15": round(self.tg11[5], 2),
                     "ttg20": round(self.tg21[0], 2), "ttg21": round(self.tg21[1], 2), "ttg22": round(self.tg21[2], 2),
                     "ttg23": round(self.tg21[3], 2), "ttg24": round(self.tg21[4], 2), "ttg25": round(self.tg21[5], 2),
                     "qQ10": round(self.Q1[0], 2), "qQ11": round(self.Q1[1], 2), "qQ12": round(self.Q1[2], 2),
                     "qQ13": round(self.Q1[3], 2), "qQ14": round(self.Q1[4], 2), "qQ15": round(self.Q1[5], 2)})

    def cal1(self):
        w1=[]
        Re1=[]
        Nu1=[]
        a1=[]
        k=[]
        C1=[]
        f=[]
        dt1=[]
        dt2=[]
        self.tg11=[]
        self.tg21=[]
        self.Q1=[]
        for i in range(len(self.G1)):
            w1.append( (4 * self.G1[i]) / (Tab_3("T", self.sourse['tvx'], "p") * pi * self.d1 ** 2 * 3600))
            w2 = (4 * self.sourse['Gn']) / (Tab_3("T", self.sourse['tn'], "p") * pi * (self.D ** 2 - self.d1 ** 2) * 3600)
            Re1.append(w1[i] * self.d1 / (Tab_3("T", self.sourse['tvx'], "v")))
            Nu1.append(0.021 * Re1[i] ** 0.8 * (Tab_3("T", self.sourse['tvx'], "Pr")) ** 0.43 * (
                    (Tab_3("T", self.sourse['tvx'], "Pr")) / (
                    Tab_3("T", (0.5 * (self.sourse['tvx'] + self.sourse['tn'])), "Pr"))) ** 0.25)
            a1.append(Nu1[i] * (Tab_3("T", self.sourse['tvx'], "lamd")) / self.d1)
            Re2 = w2 * (self.D - self.d2) / (Tab_3("T", self.sourse['tn'], "v"))
            Nu2 = 0.021 * Re2 ** 0.8 * (Tab_3("T", self.sourse['tn'], "Pr")) ** 0.43 * (
                (Tab_3("T", self.sourse['tn'], "Pr")) / (
                Tab_3("T", (0.5 * (self.sourse['tvx'] + self.sourse['tn'])), "Pr"))) ** 0.25
            a2 = Nu2 * (Tab_3("T", self.sourse['tn'], "lamd")) / self.d2
            k.append(1 / (1 / a1[i] + ((self.d2 - self.d1) / 2) / (
            Tab_3("T", (0.5 * (self.sourse['tvx'] + self.sourse['tn'])), "lamd")) + 1 / a2))
            F = self.n1 * pi * self.l * ((self.d1 + self.d2) / 2)
            C1.append(self.G1[i] * (Tab_3("T", self.sourse['tvx'], "cp")))
            C2 = self.sourse['Gn'] * (Tab_3("T", self.sourse['tn'], "cp"))
            f.append((1 - exp(k[i] * F / C1[i] * (1 - (C1[i] / C2)))) / (
                        1 - (C1[i] / C2) * exp(-k[i] * F / C1[i] * (1 - (C1[i] / C2)))))
            dt1.append((self.sourse['tvx'] - self.sourse['tn']) * f[i])
            dt2.append(dt1[i] * C1[i] / C2)
            self.tg11.append(self.sourse['tvx'] - dt1[i])
            self.tg21.append(self.sourse['tn'] - dt2[i])
            self.Q1.append(C1[i] * dt1[i])
        Word.record({"w2": round(w2*10**6, 2), "Re2": round(Re2*10**6, 2), "Nu2": round(Nu2*10**6, 2), "a2": round(a2*10**6, 2), "F": round(F, 2), "C2": round(C2, 2),
                     "w10": round(w1[0]*10**6, 2), "w11": round(w1[1]*10**6, 2), "w12": round(w1[2]*10**6, 2), "w13": round(w1[3]*10**6, 2), "w14": round(w1[4]*10**6, 2), "w15": round(w1[5]*10**6, 2),
                     "Re10": round(Re1[0]*10**6, 2), "Re11": round(Re1[1]*10**6, 2), "Re12": round(Re1[2]*10**6, 2), "Re13": round(Re1[3]*10**6, 2), "Re14": round(Re1[4]*10**6, 2), "Re15": round(Re1[5]*10**6, 2),
                     "Nu10": round(Nu1[0]*10**6, 2), "Nu11": round(Nu1[1]*10**6, 2), "Nu12": round(Nu1[2]*10**6, 2), "Nu13": round(Nu1[3]*10**6, 2), "Nu14": round(Nu1[4]*10**6, 2), "Nu15": round(Nu1[5]*10**6, 2),
                     "a10": round(a1[0]*10**6, 2), "a11": round(a1[1]*10**6, 2), "a12": round(a1[2]*10**6, 2), "a13": round(a1[3]*10**6, 2), "a14": round(a1[4]*10**6, 2), "a15": round(a1[5]*10**6, 2),
                     "k10": round(k[0]*10**6, 2), "k11": round(k[1]*10**6, 2), "k12": round(k[2]*10**6, 2), "k13": round(k[3]*10**6, 2), "k14": round(k[4]*10**6, 2), "k15": round(k[5]*10**6, 2),
                     "C10": round(C1[0], 2), "C11": round(C1[1], 2), "C12": round(C1[2], 2), "C13": round(C1[3], 2), "C14": round(C1[4], 2), "C15": round(C1[5], 2),
                     "dt10": round(dt1[0]*10**4, 2), "dt11": round(dt1[1]*10**4, 2), "dt12": round(dt1[2]*10**4, 2), "dt13": round(dt1[3]*10**4, 2), "dt14": round(dt1[4]*10**4, 2), "dt15": round(dt1[5]*10**4, 2),
                     "dt20": round(dt2[0]*10**4, 2), "dt21": round(dt2[1]*10**4, 2), "dt22": round(dt2[2]*10**4, 2), "dt23": round(dt2[3]*10**4, 2), "dt24": round(dt2[4]*10**4, 2), "dt25": round(dt2[5]*10**4, 2),
                     "tg10": round(self.tg11[0], 2), "tg11": round(self.tg11[1], 2), "tg12": round(self.tg11[2], 2), "tg13": round(self.tg11[3], 2), "tg14": round(self.tg11[4], 2), "tg15": round(self.tg11[5], 2),
                     "tg20": round(self.tg21[0], 2), "tg21": round(self.tg21[1], 2), "tg22": round(self.tg21[2], 2), "tg23": round(self.tg21[3], 2), "tg24": round(self.tg21[4], 2), "tg25": round(self.tg21[5], 2),
                     "Q10": round(self.Q1[0], 2), "Q11": round(self.Q1[1], 2), "Q12": round(self.Q1[2], 2), "Q13": round(self.Q1[3], 2), "Q14": round(self.Q1[4], 2), "Q15": round(self.Q1[5], 2)})

    def graf1(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G1, кг/ч')
        ax.set_ylabel(u'Q, Вт')
        # Добавляем заголовок графика
        ax.set_title(u'Q(G1)')
        # Рисуем линию конденсационного режима
        ax.plot(self.G1, self.Q1, label=u'Зависимость Q от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event1_Q.png')

    def graf2(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G2, кг/ч')
        ax.set_ylabel(u'Q, Вт')
        # Добавляем заголовок графика
        ax.set_title(u'Q(G2)')
        # Рисуем линию конденсационного режима
        ax.plot(self.G2, self.Q2, label=u'Зависимость Q от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event2_Q.png')

    def graf3(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G1, кг/ч')
        ax.set_ylabel(u"t'ж1, C")
        # Добавляем заголовок графика
        ax.set_title(u't(G1)')
        # Рисуем линию конденсационного режима
        ax.plot(self.G1, self.tg11, label=u'Зависимость t от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event1_t.png')

    def graf4(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G2, кг/ч')
        ax.set_ylabel(u"t'ж2, C")
        # Добавляем заголовок графика
        ax.set_title(u't(G1)')
        # Рисуем линию конденсационного режима
        ax.plot(self.G2, self.tg12, label=u'Зависимость t от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event2_t.png')

    def graf5(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G1, кг/ч')
        ax.set_ylabel(u'tж1, C')
        # Добавляем заголовок графика
        ax.set_title(u"t''(G1)")
        # Рисуем линию конденсационного режима
        ax.plot(self.G1, self.tg21, label=u'Зависимость t от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event1_t2.png')

    def graf6(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'G2, кг/ч')
        ax.set_ylabel(u'tж2, C')
        # Добавляем заголовок графика
        ax.set_title(u"t''(G2)")
        # Рисуем линию конденсационного режима
        ax.plot(self.G2, self.tg22, label=u'Зависимость t от G в противоточной схеме', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_4_event2_t2.png')

    # Эта функция сохняет данные word
    def save(self, parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        Word.record({"Name": Name, "Soursetvx": self.sourse["tvx"], "SourseGvx": self.sourse["Gvx"], "Soursetn": self.sourse["tn"],
                     "SourseGn": self.sourse["Gn"]})
        # Делаем запись в журнале
        logging.info("Начал записывать файл doxc")
        # Производим сохранение данных
        Word.save()
        # Делаем запись в журнале
        logging.info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_4")


