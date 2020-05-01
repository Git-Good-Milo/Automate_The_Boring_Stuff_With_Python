# Learning about Dictionaries
#myCat = {"size": "fat", "colour": "gray", "Disposition": "loud"}
import pprint

message = "The quick brown fox jumped over the lazy dog"
count = {} # "r": 12. Meaning the the letter "r" appears 12 times.

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) # pprint allows us to format print to make it more readable/pretty