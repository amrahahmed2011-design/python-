def match_words(words):
    ctr = 0
    lst=[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("Number of words that have first and last characters the same:", lst)
    return ctr

count = match_words(['abc', 'xyz', 'aba', '1221', 'hello', 'wow', 'noon', 'test', 'level'])
print("Count of words with matching first and last characters:", count)