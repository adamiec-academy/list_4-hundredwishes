def my_split(text):
    list = []
    text = text.strip()
    word = ""
    for i in range(len(text)):
        if text[i] == " ":
            list.append(word)
            word = ""
        elif (i+1) == len(text):
            word = word + text[i]
            list.append(word)
        else:
            word = word + text[i]
    return list
