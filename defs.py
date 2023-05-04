import shutil
import os
from docx import Document
import win32com.client as win32
import sqlite3
import datetime
import subprocess
import sys
def List_dish(category):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    category = 'первые блюда'
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=?", (category,))
    results = cursor.fetchall()
    conn.close()
    return results
def Dish(id):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    id = '3'
    cursor.execute("SELECT * FROM Dish_table WHERE Id_dish=?", (id))
    results = cursor.fetchone()
    conn.close()
    return results
#РАботает
def Sertifikat(name):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM state")
    results = cursor.fetchone()
    conn.close()
    rang=results[1]
    kolvo_b=results[0]
    date = str(datetime.date.today())

    template = "СертификатШаблон.docx"
    new_document = "Сертификат.docx"
    template_copy = "СертификатШаблон_copy.docx"

    # создаем копию оригинального документа
    shutil.copy(template, template_copy)

    # открываем копию в качестве шаблона
    doc = Document(template_copy)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if 'ИМЯ ФАМИЛИЯ' in run.text:
                run.text = run.text.replace('ИМЯ ФАМИЛИЯ', name)
            elif '1' in run.text:
                run.text = run.text.replace('1', str(rang))
            elif '9' in run.text:
                run.text = run.text.replace('9', str(kolvo_b))
            elif 'Дата' in run.text:
                run.text = run.text.replace('Дата', date)

    # сохраняем созданный документ
    doc.save(new_document)

    # удаляем копию шаблона
    os.remove(template_copy)
     
    os.startfile(new_document)
#РАботает
def Dobav_rezept(name,kategory,discription,product,level):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Dish_table (Name_dish,Name_category,Description_dish,Grocery_list, Level_dish,Favorite,Done) VALUES (?, ?, ?, ?, ?,?,?)", 
                   (name, kategory, discription,product,level,"0","0"))
    conn.commit()
    conn.close()
#РАботает
def go_to_new_file(filename):
    # Запустить новый файл в новом процессе
    os.execl(sys.executable, sys.executable, filename)

    # Закрыть текущий файл
    sys.exit()
#РАботает
def go_to_podbor(filename,product):

    subprocess.run(["python", filename, product])

    sys.exit()
#РАботает
def vabor_category(kategory,param):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=? AND Grocery_list LIKE ?", (kategory, f"%{param}%"))
    results = cursor.fetchall()
    conn.close()
    return results
def vabor_category_delete_dish(kategory,):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=?", (kategory,))
    results = cursor.fetchall()
    conn.close()
    return results
def delete_dish(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Dish_table WHERE Name_dish=?", (name_dish,))
    conn.commit() # you need to commit the changes to the database
    conn.close()
#РАботает
def vivod_recipe(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_dish=?", (name_dish,))
    results = cursor.fetchone()
    conn.close()
    return results