import pymysql  # Импорт библиотеки PyMySQL
import random

# Подключение к СУБД и выбор БД
con = pymysql.connect(host='localhost', user='root', password='', database='lab4')

with con:
    cur = con.cursor()
    print('Очищаем все таблицы')
    cur.execute("DELETE FROM aud WHERE 1")
    con.commit()
    cur.execute("DELETE FROM type WHERE 1")
    con.commit()
    cur.execute("DELETE FROM fond WHERE 1")
    con.commit()

    print()
    print('Заполняем таблицу fond (корпуса)')
    name = ('Г', 'Л', 'В', 'Б', 'А')
    for korp in name:
        qa = random.randint(300, 800)
        query = f"INSERT INTO fond (name, qa) VALUES ('{korp}', '{qa}')"
        print(query)
        cur.execute(query)
        con.commit()

    print()
    print('Заполняем таблицу type (типы аудиторий)')

    name1 = ('Лекционная', 'Практическая', 'Лабораторная', 'Техническая', 'Научная')
    kod = 0
    for name in name1:
        query = f"INSERT INTO type (kod, name) VALUES ('{kod}', '{name}')"
        kod += 1
        print(query)
        cur.execute(query)
        con.commit()

    print()
    print('Заполняем таблицу aud (аудиторий)')

    cur.execute("SELECT id FROM fond")
    rows = cur.fetchall()
    fond = []
    for row in rows:
        fond.append(row[0])
    print(fond)

    num = 0
    for i in range(100):
        typ = random.randint(0, 4)
        id_f = fond[random.randint(0, 4)]
        num += 1
        comp = random.randint(0, 100)
        if random.randint(0, 1) == 1:
            video = 'Да'
        else:
            video = 'Нет'
        vmest = random.randint(16, 100)
        query = f"INSERT INTO aud (type, id_f, num, comp, video, vmest) VALUES ('{typ}', '{id_f}', '{num}', '{comp}', '{video}', '{vmest}')"
        kod += 1
        print(query)
        cur.execute(query)
        con.commit()





