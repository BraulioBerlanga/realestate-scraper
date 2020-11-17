from conn import connection,cursor

def insertquerymieten(title,price,area,totalarea,rooms,postcode):
    QueryInsert = "INSERT INTO hausmieten (Title, Price, Area, TotalArea, Rooms, PostCode) VALUES (%s,%s,%s,%s,%s,%s)"
    InputQuery = title,price,area,totalarea,rooms,postcode
    cursor.execute(QueryInsert,InputQuery)
    connection.commit()

def insertquerykaufen(title,price,area,totalarea,rooms,postcode):
    QueryInsert = "INSERT INTO hauskaufen (Title, Price, Area, TotalArea, Rooms, PostCode) VALUES (%s,%s,%s,%s,%s,%s)"
    InputQuery = title,price,area,totalarea,rooms,postcode
    cursor.execute(QueryInsert,InputQuery)
    connection.commit()