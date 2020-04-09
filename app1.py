import json
from difflib import get_close_matches

data = json.load(open("data.json"))

i = 1

def Word():
   word = input("enter a word: ").lower()
   return word

def Word2():
   word2 = input("enter a word: ").lower()
   return translate(word2)

def translate(word):
  if word in data:
     print(data[word])
     return 0
  elif get_close_matches(word, data.keys()) != []: 
  #alt len(get_close_matches(word, data.keys()))                   
    print ("do you mean: %s" % (get_close_matches(word, data.keys())))
    return Word2()
  else:
    print("word doesn't exist, please double check") 
    return Word2()

translate(Word())