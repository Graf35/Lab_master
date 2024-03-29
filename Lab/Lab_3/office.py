#Импортируем библиотеку docxtpl. Она позволяет работать с файлами .docx
from docxtpl import DocxTemplate
#Импортируем библиотеку shutil. Она нужна для копирования файлов шаблонов в качестве основных.
import shutil

#Этот класс работает с документами .doc, ,docx
class World():
    #Объявляем пустое  хранилище, где будем хранить переменные, необходимые добавить в документ.
    b={}

    def copy(self, task):
        if task==1:
            # Копируем файлы шаблоны в качестве рабочих файлов
            shutil.copy("Labs\Lab_3_шаблон.docx", "Rezalts\Lab_3.docx")
        elif task==2:
            # Копируем файлы шаблоны в качестве рабочих файлов
            shutil.copy("Labs\Lab_32_шаблон.docx", "Rezalts\Lab_3.docx")
        elif task==3:
            # Копируем файлы шаблоны в качестве рабочих файлов
            shutil.copy("Labs\Lab_33_шаблон.docx", "Rezalts\Lab_3.docx")


    #Эта функция принимает в себя значения для записи и помещает их в хранилище
    def record(self, record):
        #Перебираем значение словаря
        for key in record:
            #Проверяем есть ли уже значение с подобным ключом в словаре
            if key in self.b:
                #Перезаписываем значение
                World.rebase(World, {key: record[key]})
            else:
                #Записываем в хранилище значение переменных
                self.b[key]=record[key]

    #Эта функция принимает в себя значения для удаления и удаляет их из хранилища
    def Delite(self, record):
        # Перебираем значение словаря
        for key in record:
            # удаляем значение
            self.b.pop(key)

    # Эта функция принимает в себя значения для удаления и удаляет их из хранилища
    def rebase(self, record):
        # Перебираем значение словаря
        for key in record:
            # удаляем значение
            self.b.pop(key)
            # Записываем новое значение в хранилище
            self.b[key] = record[key]

    #Эта функция записывает значение переменных в документ
    def save(self):
        #Активируем файл
        doc = DocxTemplate("Rezalts\Lab_3.docx")
        #Производим запись переменных в файл
        doc.render(self.b)
        #Сохраняем документ
        doc.save("Rezalts\Lab_3.docx")