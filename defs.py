import sqlite3
def List_dish():
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    category = 'первые блюда'
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=?", (category,))
    results = cursor.fetchall()
    for row in results:
        print(row[0])

    conn.close()
List_dish()