sentence = "python is easy and python is powerful"
words = sentence.split()

unique_words = set(words)       # remove duplicates
sorted_words = sorted(unique_words)

print("Unique Words:", unique_words)
print("Sorted Words:", sorted_words)
