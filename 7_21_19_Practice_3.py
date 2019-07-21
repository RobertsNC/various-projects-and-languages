def URLify(string):
    url_string = string.replace(' ', '%20')
    return url_string


s = 'asdf asd ;asdf '
print(URLify(s))
