import random
import time

stime = time.time()

def Interpolation_Search(N, T):
    InterArr = []

    y = random.sample(range(1, 32767), N)
    for i in y:
        InterArr.append(i)
        array.sort()
    print(InterArr)

    l = 0
    h = len(InterArr)-1

    while l <= h and T >= InterArr[l] and T <= InterArr[h]:
        if l == h:
            if InterArr[l] == x:
                return l;
            return -1
        POS = l + ((h-l)*(T - InterArr[l])/(InterArr[h]-InterArr[l]))

        if InterArr[POS] == T:
            return POS

        if InterArr[POS]<T:
            l = POS+1

        else:
            h = POS -1;

    return -1

    etime = time.time()

    totaltime = etime - stime
    print(totaltime)


def main():
    N = int(input("enter size of the array: "))
    T = int(input("Enter a number to search: "))

    Loc = Interpolation_Search(N, T)
    if Loc != -1:
        print(str(T) + " found at " + str(Loc))

    else:
        print(str(T)+"not found")


main()
etime = time.time()
totaltime = etime - stime
print(totaltime)