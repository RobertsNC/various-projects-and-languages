# compresses a string
s1 = 'aaaaveeaaaaaaaaaarrwer'


def s_compression(s1):
    compressed_s = ''
    curr = s1[0]
    count = 0
    for char in s1:
        if char == curr:
            count += 1
        else:
            compressed_s += curr + str(count)
            curr = char
            count = 1
    compressed_s += curr + str(count)
    if len(compressed_s) < len(s1):
        return compressed_s
    else:
        return s1


print(s_compression(s1))
