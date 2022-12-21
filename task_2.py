def my_split(text):
    list = []
    text = text.strip()
    word = ""
    for i in range(len(text)):
        if text[i] == " ":
            if text[i-1] != " ":
                list.append(word)
                word = ""
            else:
                pass
        elif (i+1) == len(text):
            word = word + text[i]
            list.append(word)
        else:
            word = word + text[i]
    return list
