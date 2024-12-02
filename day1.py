f = open("list", "r")

leftc = []
rightc = []

for x in f:
    l, r = x.split("   ")
    leftc.append(l)
    rightc.append(r)

sum = 0

leftc.sort(), rightc.sort()
for x, y in zip(leftc, rightc):
    difference = abs(int(x)-int(y))
    sum += difference

print(sum)
