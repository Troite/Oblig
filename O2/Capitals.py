a_dictionary = {}
a_file = open("USCapitals.py")

with open("USCapitals.py") as a_file:
    for line in a_file:
        key, value = line.split(", ")
        a_dictionary[key] = value
        a_dictionary[key] = value.strip()

state = input("Enter state to search for: ")

if state in a_dictionary:
    print(a_dictionary[state])
else:
    print("Error, invalid state")
