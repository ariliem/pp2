import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="jimin6"
)

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO public.phone_book("PersonName", "PhoneNumber") VALUES (%s, %s);', (name, number))

def importFromCSV():
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO public.phone_book("PersonName", "PhoneNumber") VALUES (%s, %s);', (personName, phoneNumber))

def update_contact(personName, phoneNumber):
    cur.execute('UPDATE public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (phoneNumber, personName))

def queryData():
    cur.execute('SELECT * FROM public.phone_book')
    data = cur.fetchall()
    path = r"C:\Users\aarai\Desktop\lab100\queredData.txt"

    with open(path, "w") as f:
        for row in data:
            f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")

def deleteData():
    print("Which name do you want to delete?")
    personName = input()
    cur.execute(f'DELETE FROM public.phone_book WHERE "PersonName" = %s;', (personName,))

def deleteAllData():
    cur.execute('DELETE FROM public.phone_book')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload form csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from table by person name\n\
          6. Delete all data from table\n\
          7. Exit")
    try:
        x = int(input("Enter number 1-7\n"))
        if x == 1:
            inputData()
        elif x == 2:
            importFromCSV()
        elif x == 3:
            print("Which contact do you want to update? Enter name and new number: ")
            name = input()
            newNumber = input()
            update_contact(name, newNumber)
        elif x == 4:
            queryData()
        elif x == 5:
            deleteData()
        elif x == 6:
            deleteAllData()
        elif x == 7:
            done = True
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    conn.commit()

cur.close()
conn.close()
