#cehck the string that it is symetrical or palindrome
def sp(str):
    
        half=len(str)//2
        if len(str)%2==0:
            return str[:half]==str[half:]
              
        elif str[0:]==str[::-1]:
            return "String is Palindrome"
        else:
             return "None"
        
str="kokok"
print(sp(str))