print('FOURTH')
for i in range(10):
    for k in range(i):
        print(" ", end=" ")
    for j in range(10-i):
        print("*", end=" ")
    print("")
