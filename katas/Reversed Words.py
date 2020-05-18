def reverseWords(str):
    return ' '.join(reversed(str.split()))


assert reverseWords("hello world!") == "world! hello", reverseWords("hello world!")