import json
from difflib import SequenceMatcher, get_close_matches

def similar(word1, word2_list):
    similar_word = get_close_matches(word1, word2_list, cutoff=0.8)
    if len(similar_word) > 0:
        return similar_word
    else:
        return False


def defination(word):
    word = word.lower()
    with open("your file location", "r") as myfile:
        data = json.load(myfile);
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]    
    else:
        result = similar(word, data.keys())
        if result:
            ans = input(f"\nDo you mean {result[0]} [y/n]:")
            if ans == 'y':
                return data[result[0]]
            elif ans == 'n':
                return "\nWord doesn't exist please double check it"
            else:
                return "Invalid input"
        else:
            return "\nWord doesn't exist"

ip = input("Enter any word:")
output = defination(ip)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
