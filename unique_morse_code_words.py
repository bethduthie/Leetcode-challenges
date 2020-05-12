def uniqueMorseRepresentations(words = []):
    morse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.",
             'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.",
             'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-",
             'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."}

    words_as_morse = []
    answer = set()
    for word in words:
        for i in word:
            words_as_morse.append(morse[i])
        answer.add(''.join(words_as_morse))
        words_as_morse = []

    return len(answer)


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
