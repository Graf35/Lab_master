#Импортируем настройки конфигурации записи логирования
from Lab.Lab_3 import Log
#Импортируем библиотеку для работы Microsoft offise
from Lab.Lab_3.office import World
#Импортируем файл дополнительной библиотеки
from Lab.Lab_3.File import *
#Импортируем модуль logging. Он необходим для возможности логирования.
import logging
import matplotlib.pyplot as plt

class Lab_3():
    def __init__(self):
        # Делаем запись в журнале
        logging.info("Начат расчёт лаботаторной работы 'Свободная конвекция'.")

    def Chenge(self, parent):
        if self.sourse['task']==1:
            # Применяем настройки логирования
            logger = Log.Deman_log()
            # Активируем возможность работы с файлами .doxc
            self.Word = World()
            # Делаем об этом запись в журнале.
            logging.info("Деман Word Призван!")
            self.Word.copy(self.sourse['task'])
            self.tack1(parent)
            self.save(parent)
            self.graf1()
            self.graf2()
        elif self.sourse['task']==2:
            # Применяем настройки логирования
            logger = Log.Deman_log()
            # Активируем возможность работы с файлами .doxc
            self.Word = World()
            # Делаем об этом запись в журнале.
            logging.info("Деман Word Призван!")
            self.Word.copy(self.sourse['task'])
            self.tack2(parent)
            self.save(parent)
            self.graf3()
            self.graf4()
        elif self.sourse['task']==3:
            # Применяем настройки логирования
            logger = Log.Deman_log()
            # Активируем возможность работы с файлами .doxc
            self.Word = World()
            # Делаем об этом запись в журнале.
            logging.info("Деман Word Призван!")
            self.Word.copy(self.sourse['task'])
            self.tack3(parent)
            self.save(parent)
            self.graf5()
            self.graf6()
    def tack1(self, parent):
        self.h1=[0.1, 0.5, 1, 2, 5, 10]
        s=2
        rco2=0.13
        rh2o=0.11
        rn2=0.76
        P=100
        t3=1200
        t1=20
        eps=0.8
        F1=[]
        F2=[]
        F3=[]
        V=[]
        lf=[]
        epsco2=[]
        epsh2o=[]
        b=[]
        eps3=[]
        Q1=[]
        Q3=[]
        fi12=[]
        fi21=[]
        fi22=[]
        fi31=[]
        fi32=[]
        A=[]
        B=[]
        C=[]
        D=[]
        Qf1=[]
        Qf2=[]
        Qp1=[]
        self.qp11=[]
        epspr=[]
        self.t21=[]
        for i in range(len(self.h1)):
            F1.append(s)
            F2.append(s+2*self.h1[i])
            F3.append((F1[i]+F2[i]))
            V.append(s*self.h1[i])
            lf.append(0.9*(4*V[i]/F3[i]))
            Pco2=P*rco2
            Ph2o=P*rh2o
            parent.Pixmap("Windows\monogram\CO2.png")
            parent.label_2.setText("t3="+str(t3)+"(pco2*lэф)="+str(Pco2*lf[i])+"\n По монограмме определить значение степени черноты")
            epsco2.append(float(dialog(parent)))
            parent.Pixmap("Windows\monogram\H2O.png")
            parent.label_2.setText(
                "t3=" + str(t3) + "(ph2o*lэф)=" + str(Ph2o * lf[i]) + "\n По монограмме определить значение степени черноты")
            epsh2o.append(float(dialog(parent)))
            parent.Pixmap("Windows\monogram\Be.png")
            parent.label_2.setText(
                "epsh2o=" + str(epsh2o[i]) + "p= 0.1\n По монограмме определить значение поправки")
            b.append(float(dialog(parent)))
            eps3.append(epsco2[i]+b[i]*epsh2o[i])
            Q1.append(eps*5.67*((t1+273)/100)**4*F1[i])
            Q3.append(eps3[i]*5.67*((t3+273)/100)**4*F3[i])
            fi12.append(1-eps3[i])
            fi21.append((1-eps3[i])*F1[i]/F2[i])
            fi22.append((1-eps3[i])*(1-F1[i]/F2[i]))
            fi31.append(F1[i]/F3[i])
            fi32.append(F2[i]/F3[i])
            A.append(Q1[i]+Q3[i]*fi31[i]*(1-eps))
            B.append(fi21[i]*(1-eps))
            C.append(Q3[i]*fi32[i]/(1-fi22[i]))
            D.append(fi12[i]/(1-fi22[i]))
            Qf1.append((A[i]+B[i]*C[i])/(1-B[i]*D[i]))
            Qf2.append((C[i]+D[i]*A[i])/(1-B[i]*D[i]))
            Qp1.append((Qf1[i]-(Q1[i]/eps))/(1-(1/eps)))
            epspr.append((eps*eps3[i]*(1+(1-eps3[i])*F1[i]/F2[i]))/(eps3[i]+(1-eps3[i])*(1-(1-eps3[i])*(1-eps))*F1[i]/F2[i]))
            self.qp11.append(epspr[i]*5.67*(((t1+273)/100)**4)-((t3+273)/100)**4)
            self.t21.append((100*(Qf2[i]/(5.67*F2[i]))**(1/4))-273)
        self.Word.record({"Pco2": round(Pco2, 2), "Ph2o": round(Ph2o, 2), "F11": round(F1[0], 2), "F12": round(F1[1], 2),
                              "F13": round(F1[2], 2), "F14": round(F1[3], 2), "F15": round(F1[4], 2), "F16": round(F1[5], 2),
                              "F21": round(F2[0], 2), "F22": round(F2[1], 2),"F23": round(F2[2], 2), "F24": round(F2[3], 2),
                              "F25": round(F2[4], 2), "F26": round(F2[5], 2), "F31": round(F3[0], 2), "F32": round(F3[1], 2),
                              "F33": round(F3[2], 2), "F34": round(F3[3], 2), "F35": round(F3[4], 2), "F36": round(F3[5], 2),
                              "V1": round(V[0], 2), "V2": round(V[1], 2), "V3": round(V[2], 2), "V4": round(V[3], 2), "V5": round(V[4], 2),
                              "V6": round(V[5], 2), "L1": round(lf[0], 2), "L2": round(lf[1], 2), "L3": round(lf[2], 2), "L4": round(lf[3], 2),
                              "L5": round(lf[4], 2), "L6": round(lf[5], 2), "epsco21": round(epsco2[0], 3), "epsco22": round(epsco2[1], 3),
                              "epsco23": round(epsco2[2], 3), "epsco24": round(epsco2[3], 3), "epsco25": round(epsco2[4], 3),
                              "epsco26": round(epsco2[5], 3), "epsh2o1": round(epsh2o[0], 3), "epsh2o2": round(epsh2o[1], 3),
                              "epsh2o3": round(epsh2o[2], 3), "epsh2o4": round(epsh2o[3], 3), "epsh2o5": round(epsh2o[4], 3),
                              "epsh2o6": round(epsh2o[5], 3), "B1": round(b[0], 2), "B2": round(b[1], 2), "B3": round(b[2], 2),
                              "B4": round(b[3], 2), "B5": round(b[4], 2), "B6": round(b[5], 2),"eps31": round(eps3[0], 2),
                              "eps32": round(eps3[1], 2), "eps33": round(eps3[2], 2), "eps34": round(eps3[3], 2), "eps35": round(eps3[4], 2),
                              "eps36": round(eps3[5], 2), "Q11": round(Q1[0], 2), "Q12": round(Q1[1], 2), "Q13": round(Q1[2], 2),
                              "Q14": round(Q1[3], 2), "Q15": round(Q1[4], 2),  "Q16": round(Q1[5], 2), "Q31": round(Q3[0], 2),
                              "Q32": round(Q3[1], 2), "Q33": round(Q3[2], 2), "Q34": round(Q3[3], 2), "Q35": round(Q3[4], 2),
                              "Q36": round(Q3[5], 2), "Qf11": round(Qf1[0], 2),"Qf12": round(Qf1[1], 2),"Qf13": round(Qf1[2], 2),
                              "Qf14": round(Qf1[3], 2),"Qf15": round(Qf1[4], 2),"Qf16": round(Qf1[5], 2),"Qf21": round(Qf2[0], 2),
                              "Qf22": round(Qf2[1], 2), "Qf23": round(Qf2[2], 2), "Qf24": round(Qf2[3], 2), "Qf25": round(Qf2[4], 2),
                              "Qf26": round(Qf2[5], 2), "q1": round(self.qp11[0], 2), "q2": round(self.qp11[1], 2), "q3": round(self.qp11[2], 2),
                              "q4": round(self.qp11[3], 2), "q5": round(self.qp11[4], 2), "q6": round(self.qp11[5], 2),
                              "epspr1": round(epspr[0], 2), "epspr2": round(epspr[1], 2), "epspr3": round(epspr[2], 2),
                              "epspr4": round(epspr[3], 2), "epspr5": round(epspr[4], 2), "epspr6": round(epspr[5], 2),
                              "t21": round(self.t21[0], 2), "t22": round(self.t21[1], 2), "t23": round(self.t21[2], 2),
                              "t24": round(self.t21[3], 2), "t25": round(self.t21[4], 2), "t26": round(self.t21[5], 2)})


    def tack2(self, parent):
        h2=2
        s=2
        rco2=0.13
        rh2o=0.11
        rn2=0.76
        P=100
        self.t3=[800, 1200, 1600, 2000]
        t1=20
        eps=0.8
        epsco2=[]
        epsh2o=[]
        b=[]
        eps3=[]
        Q1=[]
        Q3=[]
        fi12=[]
        fi21=[]
        fi22=[]
        A=[]
        B=[]
        C=[]
        D=[]
        Qf1=[]
        Qf2=[]
        Qp1=[]
        self.qp12=[]
        epspr=[]
        self.t22=[]
        for i in range(len(self.t3)):
            F1=s
            F2=s+2*h2
            F3=F1+F2
            V=s*h2
            lf=0.9*(4*V/F3)
            Pco2=P*rco2
            Ph2o=P*rh2o
            parent.Pixmap("Windows\monogram\CO2.png")
            parent.label_2.setText("t3="+str(self.t3[i])+"(pco2*lэф)="+str(Pco2*lf)+"\n По монограмме определить значение степени черноты")
            epsco2.append(float(dialog(parent)))
            parent.Pixmap("Windows\monogram\H2O.png")
            parent.label_2.setText(
                "t3=" + str(self.t3[i]) + "(ph2o*lэф)=" + str(Ph2o * lf) + "\n По монограмме определить значение степени черноты")
            epsh2o.append(float(dialog(parent)))
            parent.Pixmap("Windows\monogram\Be.png")
            parent.label_2.setText(
                "epsh2o=" + str(epsh2o[i]) + "p= 0.1\n По монограмме определить значение поправки")
            b.append(float(dialog(parent)))
            eps3.append(epsco2[i]+b[i]*epsh2o[i])
            Q1.append(eps*5.67*((t1+273)/100)**4*F1)
            Q3.append(eps3[i]*5.67*((self.t3[i]+273)/100)**4*F3)
            fi12.append(1-eps3[i])
            fi21.append((1-eps3[i])*F1/F2)
            fi22.append((1-eps3[i])*(1-F1/F2))
            fi31=F1/F3
            fi32=F2/F3
            A.append(Q1[i]+Q3[i]*fi31*(1-eps))
            B.append(fi21[i]*(1-eps))
            C.append(Q3[i]*fi32/(1-fi22[i]))
            D.append(fi12[i]/(1-fi22[i]))
            Qf1.append((A[i]+B[i]*C[i])/(1-B[i]*D[i]))
            Qf2.append((C[i]+D[i]*A[i])/(1-B[i]*D[i]))
            Qp1.append((Qf1[i]-(Q1[i]/eps))/(1-(1/eps)))
            epspr.append((eps*eps3[i]*(1+(1-eps3[i])*F1/F2))/(eps3[i]+(1-eps3[i])*(1-(1-eps3[i])*(1-eps))*F1/F2))
            self.qp12.append(epspr[i]*5.67*(((t1+273)/100)**4)-((self.t3[i]+273)/100)**4)
            self.t22.append((100*(Qf2[i]/(5.67*F2))**(1/4))-273)
        self.Word.record(
            {"Pco2": round(Pco2, 2), "Ph2o": round(Ph2o, 2), "F1": round(F1, 2), "F2": round(F2, 2),  "F3": round(F3, 2),
             "V1": round(V, 2),  "L1": round(lf, 2),  "epsco21": round(epsco2[0], 3), "epsco22": round(epsco2[1], 3),
             "epsco23": round(epsco2[2], 3), "epsco24": round(epsco2[3], 3),
              "epsh2o1": round(epsh2o[0], 3), "epsh2o2": round(epsh2o[1], 3),
             "epsh2o3": round(epsh2o[2], 3), "epsh2o4": round(epsh2o[3], 3),
              "B1": round(b[0], 2), "B2": round(b[1], 2), "B3": round(b[2], 2),
             "B4": round(b[3], 2),  "eps31": round(eps3[0], 2),
             "eps32": round(eps3[1], 2), "eps33": round(eps3[2], 2), "eps34": round(eps3[3], 2),
             "Q11": round(Q1[0], 2), "Q12": round(Q1[1], 2), "Q13": round(Q1[2], 2),
             "Q14": round(Q1[3], 2),  "Q31": round(Q3[0], 2),
             "Q32": round(Q3[1], 2), "Q33": round(Q3[2], 2), "Q34": round(Q3[3], 2),
             "Qf11": round(Qf1[0], 2), "Qf12": round(Qf1[1], 2), "Qf13": round(Qf1[2], 2),
             "Qf14": round(Qf1[3], 2), "Qf21": round(Qf2[0], 2),
             "Qf22": round(Qf2[1], 2), "Qf23": round(Qf2[2], 2), "Qf24": round(Qf2[3], 2),
             "q1": round(self.qp12[0], 2), "q2": round(self.qp12[1], 2),
             "q3": round(self.qp12[2], 2),
             "q4": round(self.qp12[3], 2),
             "epspr1": round(epspr[0], 2), "epspr2": round(epspr[1], 2), "epspr3": round(epspr[2], 2),
             "epspr4": round(epspr[3], 2),
             "t21": round(self.t22[0], 2), "t22": round(self.t22[1], 2), "t23": round(self.t22[2], 2),
             "t24": round(self.t22[3], 2),
             })


    def tack3(self, parent):
        h3=2
        s=2
        rco2=0.13
        rh2o=0.11
        rn2=0.76
        P=100
        t3=1200
        self.t1=[20, 200, 500, 800, 1000, 1100, 1200]
        eps=0.8
        Q1=[]
        A=[]
        Qf1=[]
        Qf2=[]
        Qp1=[]
        self.qp13=[]
        self.t23=[]
        F1 = s
        F2 = s + 2 * h3
        F3 = F1 + F2
        V = s * h3
        lf = 0.9 * (4 * V / F3)
        Pco2 = P * rco2
        Ph2o = P * rh2o
        parent.Pixmap("Windows\monogram\CO2.png")
        parent.label_2.setText(
            "t3=" + str(t3) + "(pco2*lэф)=" + str(Pco2 * lf) + "\n По монограмме определить значение степени черноты")
        epsco2=(float(dialog(parent)))
        parent.Pixmap("Windows\monogram\H2O.png")
        parent.label_2.setText(
            "t3=" + str(t3) + "(ph2o*lэф)=" + str(
                Ph2o * lf) + "\n По монограмме определить значение степени черноты")
        epsh2o=(float(dialog(parent)))
        parent.Pixmap("Windows\monogram\Be.png")
        parent.label_2.setText(
            "epsh2o=" + str(epsh2o) + "p= 0.1\n По монограмме определить значение поправки")
        b=(float(dialog(parent)))
        eps3=(epsco2 + b* epsh2o)
        for i in range(len(self.t1)):
            Q1.append(eps*5.67*((self.t1[i]+273)/100)**4*F1)
            Q3=eps3*5.67*((t3+273)/100)**4*F3
            fi12=1-eps3
            fi21=(1-eps3)*F1/F2
            fi22=(1-eps3)*(1-F1/F2)
            fi31=F1/F3
            fi32=F2/F3
            A.append(Q1[i]+Q3*fi31*(1-eps))
            B=fi21*(1-eps)
            C=Q3*fi32/(1-fi22)
            D=fi12/(1-fi22)
            Qf1.append((A[i]+B*C)/(1-B*D))
            Qf2.append((C+D*A[i])/(1-B*D))
            Qp1.append((Qf1[i]-(Q1[i]/eps))/(1-(1/eps)))
            epspr=(eps*eps3*(1+(1-eps3)*F1/F2))/(eps3+(1-eps3)*(1-(1-eps3)*(1-eps))*F1/F2)
            self.qp13.append(epspr*5.67*(((self.t1[i]+273)/100)**4)-((t3+273)/100)**4)
            self.t23.append((100*(Qf2[i]/(5.67*F2))**(1/4))-273)
        self.Word.record(
            {"Pco2": round(Pco2, 2), "Ph2o": round(Ph2o, 2), "F1": round(F1, 2), "F2": round(F2, 2), "F3": round(F3, 2),
             "V1": round(V, 2), "L1": round(lf, 2), "epsco2": round(epsco2, 3),  "epsh2o": round(epsh2o, 3),
             "B": round(b, 2),  "eps3": round(eps3, 2),
              "Q11": round(Q1[0], 2), "Q12": round(Q1[1], 2), "Q13": round(Q1[2], 2), "Q17": round(Q1[6], 2),
              "Q14": round(Q1[3], 2), "Q15": round(Q1[4], 2),  "Q16": round(Q1[5], 2), "Q3": round(Q3, 2),
              "Qf11": round(Qf1[0], 2),"Qf12": round(Qf1[1], 2),"Qf13": round(Qf1[2], 2),
              "Qf14": round(Qf1[3], 2),"Qf15": round(Qf1[4], 2),"Qf16": round(Qf1[5], 2), "Qf17": round(Qf1[6], 2),"Qf21": round(Qf2[0], 2),
               "Qf22": round(Qf2[1], 2), "Qf23": round(Qf2[2], 2), "Qf24": round(Qf2[3], 2), "Qf25": round(Qf2[4], 2),
            "Qf27": round(Qf2[6], 2), "q1": round(self.qp13[0], 2), "q2": round(self.qp13[1], 2), "q3": round(self.qp13[2], 2),
            "q4": round(self.qp13[3], 2), "q5": round(self.qp13[4], 2), "q6": round(self.qp13[5], 2), "q7": round(self.qp13[6], 2),
            "epspr": round(epspr, 2),  "t21": round(self.t23[0], 2), "t22": round(self.t23[1], 2), "t23": round(self.t23[2], 2),
            "t24": round(self.t23[3], 2), "t25": round(self.t23[4], 2), "t26": round(self.t23[5], 2), "t27": round(self.t23[6], 2)})

    def graf1(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'H, м')
        ax.set_ylabel(u'Qp1, Вт/м2')
        # Добавляем заголовок графика
        ax.set_title(u'Qp1(H)')
        # Рисуем линию конденсационного режима
        ax.plot(self.h1, self.qp11, label=u'Зависимость Q от H', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event1_q.png')

    def graf2(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u'H, м')
        ax.set_ylabel(u't2, C')
        # Добавляем заголовок графика
        ax.set_title(u't2(H)')
        # Рисуем линию конденсационного режима
        ax.plot(self.h1, self.t21, label=u'Зависимость t2 от H', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event1_t.png')

    def graf3(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't3, C')
        ax.set_ylabel(u'Qp1, Вт/м2')
        # Добавляем заголовок графика
        ax.set_title(u'Qp1(t3)')
        # Рисуем линию конденсационного режима
        ax.plot(self.t3, self.qp12, label=u'Зависимость Q от t3', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event2_q.png')

    def graf4(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't3, C')
        ax.set_ylabel(u't2, C')
        # Добавляем заголовок графика
        ax.set_title(u't2(t3)')
        # Рисуем линию конденсационного режима
        ax.plot(self.t3, self.t22, label=u'Зависимость t2 от t3', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event2_t.png')

    def graf5(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't1, C')
        ax.set_ylabel(u'Qp1, Вт/м2')
        # Добавляем заголовок графика
        ax.set_title(u'Qp1(t1)')
        # Рисуем линию конденсационного режима
        ax.plot(self.t1, self.qp13, label=u'Зависимость Q от t1', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event3_q.png')

    def graf6(self):
        # Создаём пустой график
        fig, ax = plt.subplots()
        # Добавляем сетку значений
        ax.grid()
        # Подписываем координатные оси
        ax.set_xlabel(u't1, C')
        ax.set_ylabel(u't2, C')
        # Добавляем заголовок графика
        ax.set_title(u't2(t1)')
        # Рисуем линию конденсационного режима
        ax.plot(self.t1, self.t23, label=u'Зависимость t2 от t1', color='green', marker='o')
        # Добавляем легенду
        plt.legend()
        # Показываем график
        fig.savefig('Charts\Lab_3_event3_t.png')

    # Эта функция сохняет данные word
    def save(self, parent):
        parent.label_2.setText("Введите ваши инициалы и фамилию")
        Name = dialog(parent)
        # Записываем имя автора работы
        self.Word.record({"Name": Name, "task": self.sourse['task']})
        # Делаем запись в журнале
        logging.info("Начал записывать файл doxc")
        # Производим сохранение данных
        self.Word.save()
        # Делаем запись в журнале
        logging.info("Закончил записывать файл doxc")
        parent.label_2.setText("Расчёт ОКОНЧЕН! Можете скачать файл Lab_3")