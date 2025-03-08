#remove the ith character from the string
def rem(str,i):
    return str[:i]+str[i+1:]
string="malay"
print(rem(string,2))