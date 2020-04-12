#Импортируем настройки конфигурации записи логирования
from Lab.Lab_5 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_5.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_5.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
from Sourse import Tab_3, Tab_4
#Импортируем модуль Window. Он необходим для возможности работы с оконным интерфейсом.
import matplotlib.pyplot as plt



#Применяем настройки логирования
logger=Log.Deman_log()
#Активируем возможность работы с файлами .doxc
Word=World()
#Делаем об этом запись в журнале.
logging.info("Деман Word Призван!")


class Lab_5():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Начат расчёт лаботаторной работы 'Свободная конвекция'.")
        self.q=[0.1*10**6, 0.2*10**6, 0.5*10**6, 0.8*10**6, 1*10**6, 1.2*10**6, 1.4*10**6]
        self.dt=[]
        self.a=[]

    def task1(self):
        Re=[]
        Nu=[]
        l=(Tab_3("P", self.sourse['P'], "cp")*Tab_3("P", self.sourse['P'], "p")*(Tab_3("P", self.sourse['P'], "sig")*10**(-4))*(Tab_3("P", self.sourse['P'], "T")+273))/(Tab_4("P", self.sourse['P'], "r")*Tab_4("P", self.sourse['P'], "p"))**2
        Ar=(9.81*l**3/((Tab_3("P", self.sourse['P'], "v")*10**(-6)))**2)*((Tab_3("P", self.sourse['P'], "p")-Tab_4("P", self.sourse['P'], "p"))/Tab_3("P", self.sourse['P'], "p"))
        Rekr=68*Ar**(4/9)*(Tab_3("P", self.sourse['P'], "Pr"))**(-1/3)
        qkr=(Rekr*Tab_4("P", self.sourse['P'], "r")*Tab_4("P", self.sourse['P'], "p")*(Tab_3("P", self.sourse['P'], "v")*10**(-6)))/l
        for i in range(len(self.q)):
            Re.append((self.q[i]*l)/(Tab_4("P", self.sourse['P'], "r")*Tab_4("P", self.sourse['P'], "p")*(Tab_3("P", self.sourse['P'], "v")*10**(-6))))
            if Re[i]>=10**(-2):
                Nu.append(0.125*Re[i]**0.65*(Tab_3("P", self.sourse['P'], "Pr"))**(1/3))
            else:
                Nu.append(0.0625 * Re[i] ** 0.5 * (Tab_3("P", self.sourse['P'], "Pr")) ** (1 / 3))
            self.a.append((Nu[i]*(Tab_3("P", self.sourse['P'], "lamd")*10**(-2)))/l)
            self.dt.append(self.q[i]/self.a[i])
        Word.record({"cp": round(Tab_3("P", self.sourse['P'], "cp"),2), "p1": round(Tab_3("P", self.sourse['P'], "p"),2),
                     "sig": round(Tab_3("P", self.sourse['P'], "sig")*10**(-4), 2), "T": round(Tab_3("P", self.sourse['P'], "T")+273, 2),
                     "r": round(Tab_4("P", self.sourse['P'], "r"),2), "p2":  round(Tab_4("P", self.sourse['P'], "p"),2),
                     "l": round(l, 5), "Ar": round(Ar, 2), "Re": round(Rekr, 2), "v":(Tab_3("P", self.sourse['P'], "v")*10**(-6)),
                     "qkr": round(qkr, 2), "Re1": round(Re[0], 2), "Re2": round(Re[1], 2), "Re3": round(Re[2], 2),
                     "Re4": round(Re[3], 2), "Re5": round(Re[4], 2), "Re6": round(Re[5], 2), "Re7": round(Re[6], 2),
                     "Nu1": round(Nu[0], 2), "Nu2": round(Nu[1], 2), "Nu3": round(Nu[2], 2), "Nu4": round(Nu[3], 2),
                     "Nu5": round(Nu[4], 2), "Nu6": round(Nu[5], 2), "Nu7": round(Nu[6], 2), "a1": round(self.a[0], 2),
                     "a2": round(self.a[1], 2), "a3": round(self.a[2], 2), "a4": round(self.a[3], 2), "a5": round(self.a[4], 2),
                     "a6": round(self.a[5], 2), "a7": round(self.a[6], 2), "dt1": round(self.dt[0], 2), "dt2": round(self.dt[1], 2),
                     "dt3": round(self.dt[2], 2), "dt4": round(self.dt[3], 2), "dt5": round(self.dt[4], 2), "dt6": round(self.dt[5], 2),
                     "dt7": round(self.dt[6], 2),})


    def graf1(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_ylabel(u'q, Вт/м2')
        ax.set_xlabel(u'dt, C')
        # Добавляем заголовок графика
        ax.set_title(u'q(dt)')
        # Рисуем линию конденсационного режима
        ax.plot(self.dt, self.q, label=u'Зависимость q от t', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_5_q.png')

    def graf2(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_ylabel(u'a, м/с2')
        ax.set_xlabel(u'dt, C')
        # Добавляем заголовок графика
        ax.set_title(u'a(dt)')
        # Рисуем линию конденсационного режима
        ax.plot(self.dt, self.a, label=u'Зависимость a от t', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_5_a.png')

    # Эта функция сохняет данные word
    def save(self, parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        Word.record({"Name": Name, "SourseP": self.sourse['P']})
        # Делаем запись в журнале
        logging.info("Начал записывать файл doxc")
        # Производим сохранение данных
        Word.save()
        # Делаем запись в журнале
        logging.info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_5")