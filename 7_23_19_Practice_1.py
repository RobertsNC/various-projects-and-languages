from collections import Counter
# given a string, write a function to check if it is a perm of a
# palindrome.
myString = "Mr. owl ate my Metal worm"


def is_palin_perm(input_string):
    alpha_chars = [x for x in input_string.lower() if x.isalpha()]
    counts = Counter(alpha_chars)
    num_of_odd = sum(1 for letter, cnt in counts.items() if cnt % 2)
    return num_of_odd <= 1


print(is_palin_perm(myString))
