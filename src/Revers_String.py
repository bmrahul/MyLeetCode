# def reverseString(str):
#     print(str[::-1])

def reverseString(str):
    strg = ""
    for i in str:
        strg = i + strg
    return strg.lower()


def checkPalindrom(str) -> bool:
    if str.lower() == reverseString(str):
        print(True)
    else:
        print(False)
    

checkPalindrom("Mom")