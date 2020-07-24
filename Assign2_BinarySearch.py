import random
import time

def generate_array(N):
    array = []

    x = random.sample(range(1, 32767), N)
    for i in x:
        array.append(i)
        array.sort()

    return array


def Binary_Search(array, T):

    start =time.time()
    
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


def main():
    N = int(input("enter size of the array: "))
    array = generate_array(N)
    print(array)
    T = int(input("Enter a number to search: "))


    start = time.time()
    loc = Binary_Search(array, T)
    end = time.time()
    
    if loc != -1:
        print(str(T) + " found at " + str(loc))
    else:
        print(T, 'not found')
    
    # print(start)
    # print(end)
    print("Runtime = " + str(end-start))





main()

