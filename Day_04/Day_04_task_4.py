def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_words(text):
    return " ".join(text.split()[::-1])

sentence = "Python makes coding easy"

print("Vowel Count:", count_vowels(sentence))
print("Reversed Words:", reverse_words(sentence))
