import time
import math


#Эта функиця считывает данные из файла и записывает их в словарь
def entry(fail_name):
    #Создаём пустой список
    a=[]
    #Открываем файл на прочтение
    file=open(fail_name, 'r')
    #Построчно считываем данные из файла, записываем их в список
    for line in file:
        a.append(line.strip().split())
    #Закрываем файл
    file.close()
    #Разделяем на пары:имя переменной-значение переменной
    b, c=separation(a)
    #Создаём пустой словарь
    d={}
    #Записываем в словарь парами имена и значения переменных
    for i in range(len(b)):
        d[b[i]]=c[i]
    return (d)

#Эта функция принимает значения двухмерного массива и разделяет изна два одномерных
def separation(a):
    # Создаём пустые списоки для временного хранения данных.
    b = []
    c = []
    # Записываем во временное хранилище
    for i in range(len(a)):
        #Записываем имя переменной
        b.append(a[i][0])
        #Записываем значение переменной
        c.append(float(a[i][1]))
    return (b, c)

#Эта функция ожидает и преобразует данные, полученные от пользователя через интерфейс
def dialog(parent):
    #Задаём локальную переменную, которая ожидает ввода данных
    variable = 0
    #Задаём бесконечный цикл проверки ввода
    while variable == 0:
        #Если ввода переменной не произошло то останавливаем поток на 1 сек
        time.sleep(1)
        #присваиваем переменной ожидания текущие значение на табло
        variable = parent.inpat
    #Выводим пользователю сообщение
    parent.label_2.setText("Продолжаю расчёт")
    #Стираем введенное значение из окна
    parent.inpat=0
    return (variable)

#Эта функция осуществляет сегментацию графика
def segmentation(x, y):
    #Создаём пучтой список параметров
    k=[]
    #Проверяем, можем ли мы построить прямую по 3 точкам?
    for i in range(4):
        #Если можем
        if ((x[i+1]-x[i])*(y[i+2]-y[i]))==((x[i+2]-x[i])*(y[i+1]-y[i])):
            #То проверяем, положительный ли коэфициент получился?
            if ((y[i+2]-y[i])/(x[i+2]-x[i]))>0:
                #добавляем его в список
                k.append((y[i+2]-y[i])/(x[i+2]-x[i]))
    #Проверяем, записались ли коэфициенты в список
    if k==[]:
        #если нет то проводи сегментацию по 2 точкам
        for i in range(5):
            #проверяем коэфициент на отрицательность
            if ((y[i + 1] - y[i]) / (x[i + 1] - x[i]))>0:
                #добавляем его в список
                k.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
    #возвращаем список коэфициентов
    return (k)