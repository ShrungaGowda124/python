#removal of vowels

def remove_vowels(string):
    vowels=('a','e','i','o','u')
    for x in string.lower():
        if x in vowels:
            string=string.replace(x,"")
    print(string)
string=input("enter a string: ")
remove_vowels(string)
