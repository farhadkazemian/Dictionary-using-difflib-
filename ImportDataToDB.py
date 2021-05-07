import sqlite3
import json
from pathlib import Path
import string
#Delete myapp.db in current directory before running this script to test it
def createTable():
    with sqlite3.connect("myapp.db") as conn:
        cursor = conn.cursor()
        command = "CREATE TABLE Dictionary(id int PRIMARY KEY,WORD string,MEANING string,ANTONYMS string,SYNONYMS string)"
        cursor.execute(command)
        conn.commit()
def insertDataToTable():
    with sqlite3.connect("myapp.db") as conn:
        cursor = conn.cursor()
        counter = 0
        for letter in string.ascii_uppercase:
            data = Path(f"/Users/farhadmac/Desktop/python course/project1-Dictionary/data/D{letter}.json").read_text()
            dictionary = json.loads(data)
            for word in dictionary:
                
                command = "INSERT INTO Dictionary VALUES(?, ?, ?, ?, ?)"
                cursor.execute(command, (counter, word, str(dictionary[word]["MEANINGS"]), str(dictionary[word]["ANTONYMS"]), str(dictionary[word]["SYNONYMS"])))
                conn.commit()   
                counter += 1
createTable()
insertDataToTable() 
        
