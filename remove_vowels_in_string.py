def remove(sentence):
    sentence = list(sentence)
    for i in sentence:
        if i in ['a','e','i','o','u']:
            sentence.remove(i)
    sentence = ''.join(sentence)
    return sentence


print(remove('hello world'))
