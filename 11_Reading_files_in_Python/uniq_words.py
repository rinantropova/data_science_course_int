words_set = set()
with open('anna_words.txt',encoding='UTF-8') as file:
    for word in file:
        words_set.add(word)

print(len(words_set))