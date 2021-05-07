import sqlite3
import os
import sys
import difflib
word = input("Enter your word to search it:\n").upper()


with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    command = "SELECT WORD,MEANING,ANTONYMS,SYNONYMS FROM Dictionary WHERE WORD = ?"
    cursor.execute(command, (word,))
    rows = cursor.fetchall()
    if rows != []:
        print(f"{word} is found in Dictionary")
        print("HI:\n{}".format(rows))
    else:

        command = "SELECT WORD FROM Dictionary"
        cursor.execute(command)
        words = []
        for wordInDictionary in cursor.fetchall():
            words.append(str(wordInDictionary).replace("('", "").replace("',)", ""))
        suggest = difflib.get_close_matches(word,words)
        if(len(suggest) != 0):
            print(f"Error 404: {word} is not found in Dictionary.")
            for numberOfSuggestions in range(suggest.__len__()):
                print(f"[{numberOfSuggestions}]{suggest[numberOfSuggestions]}\n")
            suggested_index = input("Enter your word proper number Or press q to Exit: ").upper()
            if(suggested_index == 'Q'):
                pass
            else:
                command = "SELECT MEANING,ANTONYMS,SYNONYMS FROM Dictionary WHERE WORD = ?"
                cursor.execute(command, (suggest[int(suggested_index)],))
                rows = cursor.fetchall()
                print(suggest[int(suggested_index)]+":")
                for row in rows:
                    print(row)
        else:
            print(f"Error 404:{word} is not found in Dictionary.Try Again")
            os.execl(sys.executable, sys.executable, *sys.argv)






