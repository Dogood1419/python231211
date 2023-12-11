strA = "파이썬은 강력해"
strB = "Python is very powerfull"

print(len(strA))
print(len(strB))
print(strA[0:3])
print(strB[:6])

print("----리스트----")
colors = ["red", "blue", "green"]
print(len(colors))
colors.append("white")
colors.extend(["red", "yello", "pink"])
print(colors)
colors.sort()
print(colors)
colors.remove("blue")
print(colors)

# 반복구문
# 디버깅할때 중단점 (Break Point)
for item in colors:
    print(item)
