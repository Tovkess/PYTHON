import math

text = input("Введіть текст для аналізу: ")

words = text.split(" ")
sentences = text.split(". ")

count_sentence = len(sentences)
word_count = len(words)

if count_sentence > 0:
    avg_words_sent = word_count / count_sentence
else:
    avg_words_sent = 0

print(f"Аналіз тексту: {text}")
print(f"Кількість речень: {count_sentence}")
print(f"Кількість слів: {word_count}")
print(f"Середня кількість слів у реченні: {math.ceil(avg_words_sent)}")