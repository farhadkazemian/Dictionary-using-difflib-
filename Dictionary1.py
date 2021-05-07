import json
import os
import sys
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
     print(f"Error 404:{word} is not found in Dictionary.Try Again")
     os.execl(sys.executable, sys.executable, *sys.argv)

