import psycopg2

try:
    connection = psycopg2.connect(host='localhost', user='postgresdb', password='qwerty', database='postgresdb')
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE users(
                       id serial PRIMARY KEY,
                        name varchar(20) NOT NULL,
                        age integer);""")
        print("DB has created")

    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO users(name,age) VALUES
                       ('DIMASTA',21),
                       ('KOLYA',33),
                       ('HOMA',69);""")
        print("values are fulling")

    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM users ;""")
        print(cursor.fetchall())




except Exception as e:
    print(e)

finally:
    if connection:
        connection.close()
        print("connection close")
