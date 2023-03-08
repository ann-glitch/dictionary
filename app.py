import json
from difflib import get_close_matches

# load json data 
my_data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in my_data:
        return my_data[word]
    elif len(get_close_matches(word, my_data.keys())) > 0: 
        return input("Sorry did you mean {} instead? Enter Y if yes, or N if no.".format(get_close_matches(word, my_data.keys())[0]))
    else:
        return "Word not found, please double check."    
    

word = input("Please enter a word you'd like to know about: ")


print(translate(word))