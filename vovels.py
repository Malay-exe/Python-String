#print the string which contains vovels
def vov(str):
    x=set("a,e,i,o,u,A,E,I,O,U")
    for i in str:
        if i in x:
            return True
       
    return False
string="rythm"
print(vov(string))