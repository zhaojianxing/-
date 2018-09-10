for i in range(10):
    for j in range(0,i):
        print("-",end=" ")

    for j in range(i,10):
        print("$", end=" ")

    print("")

print("打印右上角三角形")


for i in range(10):
    for j in range(0, 10 - i):
        print("-", end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")

    print("")
print("打印右下三角形")


for i in range(10):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")

    print("")

print("打印正三角形")


for i in range(10):
    for j in range(0,i):
        print(end=" ")

    for j in range(i,10):
        print("$", end=" ")

    print("")

print("打印倒三角")
