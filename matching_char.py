#find the matching characters from the two strings
def match(str1,str2):
    x=set(str1.lower())
    y=set(str2.lower())
    z=(x.intersection(y))
    return (z) 
string1="malay"
string2="malayam"
print(match(string1,string2))