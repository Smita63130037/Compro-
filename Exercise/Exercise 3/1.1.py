#String "fgh" is in "dgdhjdghdf"

x = "dgdhjdghdf"
y = "fgh"
for i in range(len(x)):
    check1 = x[i:i+3]
    if check1 == y:
       Ans = 1
       break
    else:
       Ans = -1
print(Ans)



