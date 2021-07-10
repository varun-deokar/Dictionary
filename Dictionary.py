import json
import difflib


# The below logic is used to convert the keys from the original file to lowercase in the new file

# dic = {}
# with open("original.json", "r") as original:
#     old = json.load(original)
#     for key in old:
#         dic[key.lower()] = old[key]
#     with open("new.json", "w") as new:
#         json.dump(dic, new)
# original.close()


def check():
    for i in range(len(data[word])):
        print(data[word][i])
    return input("Type q to quit\n")


e = "a"  # Random value
with open("new.json") as new:
    data = json.load(new)
new.close()
while e != 'q':
    word = input("Enter word to search for\n").lower()
    if word in data:
        e = check()
    else:
        word = difflib.get_close_matches(word, data, n=1)  # Returns list with one element
        if len(word) != 0:
            word = word[0]
            print("Did you mean " + word)
            a = input("Type y for yes").lower()
            if a == 'y':
                e = check()
        else:
            print("No such word found. Try again")
