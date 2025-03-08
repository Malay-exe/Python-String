#reverse the sentence
def rev(s):
    x=s.split()[::-1]
    a=[]
    for i in x:
        a.append(i)
    return " ".join(a)#or return a
string="malay is a good boy"
print(rev(string))