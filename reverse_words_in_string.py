def reverseWords(sentence):
    seperate = sentence.split(' ')
    for word in range(len(seperate)):
        seperate[word] = seperate[word][::-1]
    return " ".join(seperate)
