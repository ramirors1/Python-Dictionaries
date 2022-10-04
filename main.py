programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#Adding items to the dictionary
programming_dictionary["Loop"] = "The action of doing something repeatedly"

#Retrieving items from a dictionary
#print(programming_dictionary)

#Creating an empty dictionary
empty_dictionary = {}

#Wiping a dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#editing an item in a dictionary
programming_dictionary["Bug"] = "A big boo boo"
#print(programming_dictionary)

#Looping through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])