from collections import Counter

word_count = 0
letter_count = 0
percent = []

text = open("Odyssey.txt", 'r', encoding="utf-8")
text_lis = []
text_lis_count = []

for line in text:
    text_lis.append(line)

text_lis = str(text_lis)

for word in text_lis.split():
    clear_word = ""
    word_count += 1
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()
            letter_count += 1
    text_lis_count.append(clear_word)

print(word_count)
print(letter_count)
print(letter_count / word_count)
n = Counter(text_lis_count)

for i in n:
    p = n[i]
    a = p * 100 / word_count
    percent.append(a)
percent = sorted(percent, reverse=True)
print(percent)

