import random
import time
stime = time.time()

def Binary_Search(N, T):
    #stime = time.time()

    array = []
    x = random.sample(range(1, 32767), N)
    for i in x:
        array.append(i)
        array.sort()
    print(array)
    L = 0
    H = len(array)-1
    #T = array[-1]

    ##print(L, H)

    while L <= H:
        mid = (L+H)//2

        if array[mid] == T:
            return mid
            #print("Element present at index: ", mid)
        elif array[mid] < T:
            L = mid+1
        elif array[mid] > T:
            H = mid-1
            
    return -1

    ftime = time.time()
    ttime = ftime - stime
    print("Search was executed in: ", ttime)


def main():
    N = int(input("enter size of the array: "))
    T = int(input("Enter a number to search: "))

    loc = Binary_Search(N, T)
    if loc != -1:
        print(str(T) + " found at " + str(loc))
    else:
        print(T, 'not found')



main()
etime = time.time()

totaltime = etime - stime
print(totaltime)

