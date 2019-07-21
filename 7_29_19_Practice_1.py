non_unq_string = 'aasfasfsdffsfd'
unq_string = 'asdfghjqwertyuiop'

def is_unique(string):
    seen_letters = []
    for letter in string:
        if letter in seen_letters:
            print('letter:', letter, 'is repeated')
            return
        seen_letters.append(letter)
    print('The string does not contain any repeat chars')
    return

is_unique(unq_string)