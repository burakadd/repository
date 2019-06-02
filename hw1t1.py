_str = (input("your string = "))
if _str.replace(" ", "") == _str.replace(" ", "")[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")