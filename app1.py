import json
from difflib import get_close_matches

data = json.load(open("data.json"))

i = 1

word = input("enter a word: ").lower()

def Word2():
   word2 = input("please try again: ").lower()
   return translate(word2)

def Permission():
  permission = input("wanna try again? type Y for yes or N for no: ")
  if permission == "Y":
    return Word2()
  else: 
    return 0

def translate(word):
  if word in data:
     print(data[word])
     return 0
  elif get_close_matches(word, data.keys()) != []: 
  #alt len(get_close_matches(word, data.keys()))                   
    print ("do you mean '%s'" % get_close_matches(word, data.keys())[0])
    chance = input("type Y for yes or N for no: ")
    if chance == "Y":
      translate(get_close_matches(word, data.keys())[0])
    elif chance == "N":
      Permission()
  else:
    print("word doesn't exist") 
    return Permission()

translate(word)