text=input("Please enter the string: ")

def create_dict(x):
    d = {}
    for letter in x:
        d[letter] = 1 + d.get(letter, 0)
    return d

def most_frequent(text):
    letters = [letter.lower() for letter in text]
    d = create_dict(letters)
    result = []
    for key in d:
        result.append((d[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter,"=", count)

most_frequent(text)
