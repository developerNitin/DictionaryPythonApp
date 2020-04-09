import json
from difflib import get_close_matches

data = json.load(open("data.json"))

i = 1

def Word():
   word = input("enter a word: ").lower()
   return word

def translate(word):
  if word in data:
     print(data[word])
     return 0
  elif get_close_matches(word, data.keys()) != []:                    #alt len(get_close_matches(word, data.keys()))
    print ("do you mean: %s" % (get_close_matches(word, data.keys())))
    return Word()
  else:
    print("word doesn't exist, please double check") 
    return Word()

translate(Word())