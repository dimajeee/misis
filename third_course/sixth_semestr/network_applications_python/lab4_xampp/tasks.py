import pymysql  # Импорт библиотеки PyMySQL
import random

# Подключение к СУБД и выбор БД
con = pymysql.connect(host='localhost', user='root', password='', database='lab4')

with con:
    cur = con.cursor()
    print('Список всех корпусов, отсортированных по алфавиту:')
    cur.execute("SELECT name FROM fond ORDER BY name ASC")
    result = cur.fetchall()
    for row in result:
        print(row[0])

    print('\nСписок всех типов аудиторий, отсортированных по коду в обратном порядке:')
    cur.execute("SELECT * FROM type ORDER BY kod DESC")
    result = cur.fetchall()
    for row in result:
        print(row)

    print('\nСписок всех аудиторий, отсортированных по номеру аудитории (первые пять):')
    cur.execute("SELECT * FROM aud ORDER BY num ASC LIMIT 5")
    result = cur.fetchall()
    for row in result:
        print(row)

    print('\nКоличество аудиторий:')
    cur.execute("SELECT COUNT(*) FROM aud")
    result = cur.fetchone()
    print(result[0])

    print('\nСписок уникальных вместимостей аудиторий, отсортированных по возрастанию:')
    cur.execute("SELECT DISTINCT vmest FROM aud ORDER BY vmest ASC")
    result = cur.fetchall()
    for row in result:
        print(row[0])

    print('\nНомер аудитории с минимальной вместимостью:')
    cur.execute("SELECT num FROM aud ORDER BY vmest ASC LIMIT 1")
    result = cur.fetchone()
    print(result[0])

    print('\nИнформация об аудитории, указанной пользователем:')
    user_input = input("Введите номер аудитории: ")
    cur.execute("SELECT * FROM aud WHERE num = %s", (user_input,))
    result = cur.fetchone()
    if result:
        print("Информация об аудитории:")
        print(f"Номер: {result[0]}")  # type
        print(f"Проектор: {result[5]}")  # video
        print(f"Вместимость: {result[4]}")  # vmest
        cur.execute("SELECT name FROM fond WHERE id = %s", (result[2]))
        corp_name = cur.fetchone()
        print(f"Корпус: {corp_name[0]}")  # corp
        cur.execute("SELECT name FROM type WHERE kod = %s", (0))
        corp_name = cur.fetchone()
        print(f"Тип: {corp_name}")  # id
    else:
        print("Аудитория с таким номером не найдена.")

    con.commit()


