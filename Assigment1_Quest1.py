import random

def DotPro(N, ListA, ListB):
    
        for i  in range(0, N):
             x = random.randint(1, 1000)
             ListA.append(x)
        print(ListA)

        for j in range(0,N):
             y = random.randint(1, 1000)
             ListB.append(y)
        print(ListB)

        for k in ListA:
            for l in ListB:
                z = k*l
        ListC.append(z)
        print(ListC)

ListA = []
ListB = []
ListC = []


DotPro(5, ListA, ListB)
