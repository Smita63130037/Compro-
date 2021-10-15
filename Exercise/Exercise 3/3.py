i = 0
for x in range(1,32):
    if x % 2 == 1:
        i += 1
j = 0
for y in range(1,29):
    if y % 2 == 0:
        j += 1
k = 0
for z in range(1,31):
    if z % 2 == 1:
        k += 1
print(i*7+j+k*4)
