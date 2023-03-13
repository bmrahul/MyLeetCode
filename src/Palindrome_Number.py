def isPalindrome(x: int) -> bool:
    if x == reverseNumber(x):
        return True
    else:
        return False

def reverseNumber(num: int) -> int:
    reversed_number = 0
    if num > 0:
        while num != 0:
            digit = num % 10
            reversed_number = reversed_number * 10 + digit
            num //= 10
    return reversed_number

def stringReverse(_str):
    string = ""
    for i in _str:
        string = i + string
    return string

def reverseStringUsingExtendedSlice(str):
    return str[::-1]




# isPalindrome(10)

stringReverse('Rahul')