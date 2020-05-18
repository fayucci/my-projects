def find_missing_letter_2(chars):
    chars_codes = list(map(ord, chars))
    i = chars_codes[0]
    for char_code in chars_codes:
        if i != char_code:
            return chr(i)
        i += 1
    return None



def find_missing_letter(chars):
    for (char_code, counter) in zip(map(ord, chars), range(len(chars))):
        if char_code != (counter + ord(chars[0])):
            return chr(counter + ord(chars[0]))
        

assert find_missing_letter(['a','b','c','d','f']) == 'e', 'sino la cague'

assert find_missing_letter(['a', 'b', 'c']) == None