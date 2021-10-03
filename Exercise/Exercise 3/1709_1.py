#Is in string
str1 = input("Input First String: ")
str2 = input("Input Second String: ")
L1 = len(str1)
L2 = len(str2)
Ans = -1

for i in range(L2-L1+1):
    check = 1
    for j in range(L1):
        if str1[j] != str2[i+j]:
            check = 0
    if check == 1:
        Ans = 1
        break
print(Ans)






