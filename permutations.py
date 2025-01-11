#find all the permutations of the string
def permu(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i in range(len(s)):       
        for j in permu(s[:i] + s[i+1:]):
            perms.append(s[i] + j)
    return perms

print(permu("Malay"))
