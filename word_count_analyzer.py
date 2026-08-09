from collections import Counter

file = open("sample.txt", "r")

text = file.read().lower()

# Remove simple punctuation
text = text.replace(".", "")
text = text.replace(",", "")

words = text.split()
print("Aditi Vadd\nRoll No:14")
# Total words
print("Total Words:", len(words))

# Word frequency
frequency = Counter(words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

# Most frequent word
most_frequent = frequency.most_common(1)

print("\nMost Frequent Word:", most_frequent[0][0])
print("Frequency:", most_frequent[0][1])

file.close()