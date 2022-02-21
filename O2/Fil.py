with open("1.py") as f:
    content1 = f.read()
    words1 = content1.split(" ")
    unique_words1 = set(words1)

with open("2.py") as f:
    content2 = f.read()
    words2 = content2.split(" ")
    unique_words2 = set(words2)

unique_words1_2 = unique_words1.union(unique_words2)

unique_words1_no2 = unique_words1 - unique_words2

unique_words2_no1 = unique_words2 - unique_words1

unique_words1_2_nocommon = unique_words2_no1 | unique_words1_no2

print(
    "1 - File 1 containts {} unique words and File 2 contains {} unique words".format(
        len(unique_words1), len(unique_words2)
    )
)

print(
    "2 - The unique words in file 1 and file 2 are: {}{}".format(
        unique_words1, unique_words2
    )
)

print(
    "3 - The unique words that occur in both file 1 and file 2 are: {}".format(
        unique_words1_2
    )
)

print(
    "4 - The unique words that occur in file 1, but not in file 2 are: {}".format(
        unique_words1_no2
    )
)

print(
    "5 - The unique words that occur in file 2, but not in file 1 are: {}".format(
        unique_words2_no1
    )
)

print(
    "6 - The unique words that occur in either file 1 or 2, but not in both are: {}".format(
        unique_words1_2_nocommon
    )
)
