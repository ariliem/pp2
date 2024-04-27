import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

def queryData():
    cur.execute("SELECT * FROM get_records_by_pattern('John')")
    data = cur.fetchall()

    for row in data:
        print(row)

def insertData():
    personName = input('Input new username: ')
    phoneNumber = input('Input new phone number: ')
    conn.autocommit = True 
    cur.execute("CALL insert_data(%s, %s);", (personName, phoneNumber))


def updateData():
    personName = input('Input the name of the user that you want the update her/his number: ')
    phoneNumber = input('Input the new phone number: ')
    conn.autocommit = True 
    cur.execute("CALL update_data(%s, %s);", (personName, phoneNumber))

def insertListOfDate():
    users = [
        ['Stark', '80789013456'],
        ['Admin', '80779903663'],
        ['Sasha', '80779903663p']
    ]
    print('The incorrect data')
    cur.execute(f"CALL insert_list_of_users(ARRAY{users})")
    cur.execute(" SELECT * FROM postgres.public.phone_book_incorrect_data ")
    data = cur.fetchall()

    for row in data:
        print(row)

def getDataFromPagination():
    limit = 3
    offset = 0

    # Define the cursor and call the function
    cur.execute('SELECT * FROM paginating(%s, %s)', (limit, offset))
    # conn.autocommit = True 
    data = cur.fetchall()
    k = 1
    for i in data:
        print(f"{k}.Name: {i[1]}, number: {i[2]}")
        k += 1
    # print(data)

def deleteDataWithNameOrPhone():
    mode = ''
    x = input("With what parameter you want to delete the person from phonebook?\n1 - with username\n2 - with number\n")
    if(x == '1'):
        mode = 'username'
        name = input('Input the username: ')
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (mode, name))
    if(x == '2'):
        mode = 'phone'
        number = input('Input the phone number: ')
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (mode, number))



print("What do you want to do?\n\
      1. Return data from the table\n\
      2. Insert contact\n\
        2.1 update existing contact\n\
      3. Insert list of users\n\
      4. Query all data from table\n\
      5. Delete with user name or number")
x = input("Enter number 1-5\n")
if(x == '1'):
    queryData()
elif(x == '2'):
    insertData()
elif(x == '2.1'):
    updateData()
elif(x == '3'):
    insertListOfDate()
elif(x == '4'):
    getDataFromPagination()
elif(x == '5'):
    deleteDataWithNameOrPhone()
conn.commit()
    
cur.close()
conn.close()
# cur.execute(' DELETE FROM postgres.public.phone_book ')


