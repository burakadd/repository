_str = input("your string = ")
if _str.replace(" ", "") == _str.replace(" ", "")[::-1]:
    print("{} is palindrome".format(_str))
else:
    print("{} is not palindrome".format(_str))
