from collections import Counter

s1 = input("Enter the first string: ")
count1 = Counter(s1)

s2 = input("Enter the second string: ")
count2 = Counter(s2)

if count1 == count2:
    print("The two strings ARE anagrams!")
else:
    print("The two strings ARE NOT anagrams!")
