import psycopg2
import csv 
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    def inputData():
        name = input("Hello input your name: ")
        number = input("Input your phone number: ")
        cur.execute(' INSERT INTO public.phone_book("PersonName", "PhoneNumber") VALUES( %s, %s); ' , (name, number))

    def importFromCSV():
        with open("info.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                personName, phoneNumber = row
                cur.execute(' INSERT INTO phonebook.public.phone_book("PersonName", "PhoneNumber") VALUES( %s, %s); ', (personName, phoneNumber))


    def update_contact(personName, phoneNumber):
        cur.execute(' UPDATE phonebook.public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s ', (phoneNumber, personName))

    def queryData():
        cur.execute(' SELECT * FROM phonebook.public.phone_book ')
        data = cur.fetchall()
        path = r"C:\Users\aarai\Desktop\lab100\queredData.txt"

        f = open(path, "w")
        for row in data:
            f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")
        f.close()

    def deleteData():
        print("Which name do you want to delete?\n")
        personName = input()
        cur.execute(f''' DELETE FROM phonebook.public.phone_book WHERE "PersonName"='{personName}' ''')

    def deleteAllData():
        cur.execute(' DELETE FROM phonebook.public.phone_book ')

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
        x = int(input("Enter number 1-5\n"))
        if(x == 1):
            inputData()
        elif(x == 2):
            importFromCSV()
        elif(x == 3):
            print("Which number do you want to update? Enter name and new number: ")
            name = input()
            newNumber = input()
            update_contact(name, newNumber)
        elif(x == 4):
            queryData()
        elif(x == 5):
            deleteData()
        elif(x == 6):
            deleteAllData()
        elif(x == 7):
            done = True
        conn.commit()
        
    cur.close()
    conn.close()
