#remove the ith character
def rem(str):
    x=str.replace("l"," ")
    return x
string="malay"
print(rem(string))
#another method
def remo(str):
    s=""
    for i in str:
        if i!="l":
            s+=i
    return s  
string="malay"
print(remo(string))      
