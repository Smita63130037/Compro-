##String "fghhfhfdjdu" is in "hhfhf"

x = "fghhfhfdjdu"
y = "hhfhf"
for i in range(len(x)):
    check1 = x[i:i+5]
    if check1 == y:
        Ans = 1
        break
    else:
        Ans = -1
print(Ans)


