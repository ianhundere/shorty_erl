def unshorten(code):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    url = ""
    while(code > 0):
        url += map[code % 62]
        code //= 62
    return url[len(url):: -1]


def shorten(url):
    code = 0
    for i in url:
        inc = ord(i)
        if(inc >= ord('a') and inc <= ord('z')):
            code = code*62 + inc - ord('a')
        elif(inc >= ord('A') and inc <= ord('Z')):
            code = code*62 + inc - ord('Z') + 26
        else:
            code = code*62 + inc - ord('0') + 52
    return id


if (__name__ == "__main__"):
    code = 12345
    url = shorten(code)
    print(f"short url is : {url}")
    print(f"code from {url} is {shorten(url)}")
