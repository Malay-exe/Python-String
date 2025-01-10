#find the vevn words from the string
def find(str):
    x=str.split(" ")
    for i in x:
        if len(i)%2==0:
             print(i)
string="malay is pro boy"
(find(string))        