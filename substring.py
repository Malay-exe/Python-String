#check that substring is presnt in given string
def chk(sub_str,str):
    return True if sub_str in str else False
s_string="pro"
string="Malay is a pro boy"
print(chk(s_string,string))