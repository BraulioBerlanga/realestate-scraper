import psycopg2

connection = psycopg2.connect(
    password='3179billace',
    user='postgres',
    host="localhost",
    port="5432",
    database="HauseHamburg")

cursor = connection.cursor()