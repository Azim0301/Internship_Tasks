data = ["Python", "Java", "Python", "C", "Java", "Python"]

frequency = {
    lang: data.count(lang)
    for lang in set(data)
}

print("Language Frequency:")
print(frequency)
