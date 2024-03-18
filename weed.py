def main():
    quadrat = initQuad(5,5)
    quadrat = fillQuad(quadrat)
    printQuad(quadrat)
    totalWeeds = sumQuad(quadrat)
    print(f"\nThe total number of weeds in the garden is {totalWeeds}")


def initQuad(x,y):
    quadrat = {}
    for i in range(1,y+1):
        quadrat[i] = {}
        for j in range(1,x+1):
            quadrat[i][j] = 0
    return quadrat

def fillQuad(quadrat):
    for i in quadrat:
        for j in quadrat[i]:
            quadrat[i][j] = int(input(f"Please enter the number of weeds occuring at ({j},{i})."))
    return quadrat

def printQuad(quadrat):
    print("   ",end="")
    for i in quadrat:
        print(i,end=" ")
    print("")
    for i in quadrat:
        print(i,end=": ")
        for j in quadrat[i]:
            print(quadrat[i][j],end=" ")
        print("")

def sumQuad(quadrat):
    total = 0
    for i in quadrat:
        for j in quadrat[i]:
            total += quadrat[i][j]
    return total

if __name__ == "__main__":
    main()