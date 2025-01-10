#check the string is palindrome is not
def pal(str):
    return str[0:]==str[::-1]
string="malayalam"
print(pal(string))