def string_reverse(text):

    text_token = list(text)

    l = 0
    r = len(text)-1

    special_set = []

    while l < r:
        while not text_token[l].isalpha():
            l += 1
        while not text_token[r].isalpha():
            r -= 1
        print(l,r)
        # reverse string
        text_token[l], text_token[r] = text_token[r], text_token[l]
        l += 1
        r -= 1

    text = "".join(text_token)

    return text





