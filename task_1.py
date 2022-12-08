def is_palindrome(text):
    palindrome = True
    text = text.lower().split()
    new =""
    for i in range(len(text)):
        new = new + text[i]
    for i in range(len(new)//2):
        if new[i] != new[-(i+1)]:
            palindrome = False
    return palindrome
