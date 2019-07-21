string_1 = 'asdfg'
string_2 = 'gfds2a'


def check_if_perm(string_1, string_2):
    sorted_1 = ''.join(sorted(string_1))
    sorted_2 = ''.join(sorted(string_2))
    if sorted_1 == sorted_2:
        return True
    else:
        return False


check_if_perm(string_1, string_2)
