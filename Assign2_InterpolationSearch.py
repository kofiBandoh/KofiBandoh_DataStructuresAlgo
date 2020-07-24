import random
import time

def generate_array(N):
    InterArr = []

    y = random.sample(range(1, 32767), N)
    for i in y:
        InterArr.append(i)
        InterArr.sort()
    
    return InterArr

def Interpolation_Search(InterArr, T):

    l =  0
    h = len(InterArr)-1


    while l <= h and T >= InterArr[l] and T <= InterArr[h]:
        if l == h:
            if InterArr[l] == T:
                return l
            return -1
        POS = l + ((h-l)*(T - InterArr[l])//(InterArr[h]-InterArr[l]))

        if InterArr[POS] == T:
            return POS

        if InterArr[POS]<T:
            l = POS+1

        else:
            h = POS -1

    return -1


def main():
    N = int(input("enter size of the array: "))

    InterArray = generate_array(N)

    print(InterArray)

    T = int(input("Enter a number to search: "))

    start = time.time()
    Loc = Interpolation_Search(InterArray, T)
    end = time.time()

    if Loc != -1:
        print(str(T) + " found at " + str(Loc))

    else:
        print(str(T)+" not found")

    print("Runtime = " + str(end-start))


main()