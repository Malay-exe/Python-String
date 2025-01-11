#print the duplicate characters from the string
def dup(str):
    x=""
    y=""
    for i in str:
        if i not in x:
            x+=i
        else:
            y+=i    
    return x,y
string="malay"
print(dup(string))        