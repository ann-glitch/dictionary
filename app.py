import json
from difflib import get_close_matches

# load json data 
my_data = json.load(open("data.json"))

def wordfinder(word):
    word = word.lower()

    if word in my_data:
        return my_data[word]

    elif len(get_close_matches(word, my_data.keys())) > 0: 
        entry = input("Sorry did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(word, my_data.keys())[0]))

        if entry == "Y":
            return my_data[get_close_matches(word, my_data.keys())[0]]

        elif entry == "N":
            return "Word not found, please double check."  

        else:
            return "Sorry, we did not understand your input."  

    else:
        return "Word not found, please double check."    
    

word = input("Please enter a word you'd like to know about: ")


output = wordfinder(word)

# return each definitions on a new line.
if type(output) == list:
    for item in output:
        print(item)
else:
        print(output)    