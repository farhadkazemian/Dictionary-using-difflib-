import json
import os
import sys
import difflib
from pathlib import Path

word = input("Enter your word to search it:\n").upper()

try:
    data = Path(f"/Users/farhadmac/Desktop/python course/project1-Dictionary/data/D{word[0]}.json").read_text()
except:
    print("****Something's Wrong:/ \n*******You probably write wrong word...Please start your word with standard alphabet")
    os.execl(sys.executable, sys.executable, *sys.argv)

dictionary = json.loads(data)
if word in dictionary:
    print(f"{word} is found in Dictionary")
    print("Meaning:{}".format(dictionary[word]))
else:
    suggest = difflib.get_close_matches(word, dictionary)
    if (suggest.__len__()>0):
        print(f"Error 404: {word} is not found in Dictionary.")
        for numberOfSuggestions in range(suggest.__len__()):
            print(f"[{numberOfSuggestions}]{suggest[numberOfSuggestions]}\n")
        suggested_index = input("Enter your word proper number Or press q to Exit: ").upper()
        if(suggested_index == 'Q'):
            pass        
        else:
            print("\n{} : {}".format(suggest[numberOfSuggestions], dictionary[suggest[int(suggested_index)]]))
    else:
        print("Nothing Found Search Again")
        os.execl(sys.executable, sys.executable, *sys.argv)
