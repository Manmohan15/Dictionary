import mysql.connector

con = mysql.connector.connect(
user = "root",
password = "",
host = "localhost",
database = "Dictionary"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Meaning FROM Dictionary WHERE Word = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")