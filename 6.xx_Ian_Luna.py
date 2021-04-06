# 6.xx_Ian_Luna.py | ian luna | 2020.05.06 | 2-D List

def printBackward(List2D):
    length1 = len(List2D)
    for i in range(len(List2D)):
        length1 -= 1
        length2 = len(List2D[i])
        for y in range(len(List2D[i])):
            length2 -= 1
            print(List2D[length1][length2], end='')
        print()

def printForward(List2D):
    for k in List2D:
        for c in k:
            print(c, end='')
        print()

def main():
   L2D = [[1,2,3],[4,5,6],[7,8,9]]
   printForward(L2D)
   print()
   printBackward(L2D)

if __name__ == "__main__":
    main()
