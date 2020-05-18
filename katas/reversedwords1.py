def reverse_words(text):
    return ' '.join(map(''.join, map(reversed, text.split(' '))))
    #    return ' '.join(map(lambda word: ''.join(reversed(word)), text.split()))


assert reverse_words('apple apple') == 'elppa elppa', reverse_words("hello world!")

assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow', 'se cago'