"""Challenge, out of 3 edit types
(insert rm or replace) given 2 strings
see if they differ by 1 operation"""
string_1, string_2 = 'asdf', 'bsdf'


def one_away(s1, s2):
    flag = True
    if len(s1) != len(s2):
        if len(s1) == len(s2) + 1:
            flag = check_insert(s1, s2)
        elif len(s1) == len(s2) - 1:
            flag = check_remove(s1, s2)
        else:
            flag = False

    elif len(s1) == len(s2):
        count_diff = 1
        for x, y in s1, s2:
            if s1[x] != s2[y]:
                count_diff += 1
        if count_diff > 1:
            flag = False

    return flag


def check_insert(s1, s2):
    return True


def check_remove(s1, s2):
    return True


print(one_away(string_1, string_2))
