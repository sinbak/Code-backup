import sys
import random
import time
import copy
#과제 1번
N, M = input("N M = ").split()
N = int(N)
M = int(M)
numList = []
test = []
def Sort(N,M):
    if N<= 10 and M <= 10: #출력 조건
        for i in range(1, N+1):
            test.append(i)
        test.sort()
        for j in range(M):
            if j == 0:
                numList.append(test)
                print("T"+ str(j)+": " + ' '.join(map(str,test)))
            elif j == 1:
                test.reverse()
                numList.append(test)
                print("T"+ str(j)+": " + ' '.join(map(str,test)))
            else:
                random.shuffle(test)
                numList.append(test.copy())
                print("T"+ str(j)+": " +' '.join(map(str,test)))
    else:
        print("{} test case inputs generated.".format(M))
        print("{} integers in each test case.".format(N))
        for i in range(1, N+1):
            test.append(i)
        test.sort()
        for j in range(M):
            if j == 0:
                numList.append(test)
            elif j == 1:
                test.reverse()
                numList.append(test)
            else:
                random.shuffle(test)
                numList.append(test.copy())
        

def get_exec_time(func, *args, **kargs):
    start = time.time()
    func(*args, **kargs)
    milliend = (time.time() - start)*1000
    return milliend


def get_comparison_time(func, lst: list, print_result: bool = False):
    best = 1000000
    worst = 0
    total = 0

    for a in lst:
        b = get_exec_time(func, a)
        total += b
        if best > b:
            best = b
        if worst < b:
            worst = b

    avg = total / len(lst)

    if print_result:
        print("Best\t:{:.5f}".format(best))
        print("Worst\t:{:.5f}".format(worst))
        print("Average\t:{:.5f}".format(avg))
    return [best, worst, avg]

def Bubble_sort(numList):
    numList_C = numList.copy()
    if N <= 10 and M <= 10:
        for i in range(len(numList_C)):
            print("L" + str(i)+ ": " + ' '.join(map(str,numList_C)))
            for j in range(len(numList_C)-i-1):
                if numList_C[j]>numList_C[j+1]:
                    check = numList_C[j+1]
                    numList_C[j+1]=numList_C[j]
                    numList_C[j]=  check
    else:
        start = time.time()
        for i in range(len(numList_C)):
            for j in range(len(numList_C)-i-1):
                if numList_C[j]>numList_C[j+1]:
                    check = numList_C[j+1]
                    numList_C[j+1]=numList_C[j]
                    numList_C[j]=  check

        return numList_C

def Selection_sort(numList):
    numList_C = numList.copy()

    if N <= 10 and M <= 10:
        for i in range(len(numList_C)-1, -1, -1):
            max_idx = 0
            print("L" + str(len(numList_C)-i-1)+ ": " + ' '.join(map(str,numList_C)))
            for j in range(1, i+1):
                if numList_C[j] > numList_C[max_idx]:
                    max_idx = j
            check = numList_C[i]
            numList_C[i] = numList_C[max_idx]
            numList_C[max_idx] = check
    else:
        start = time.time()
        for i in range(len(numList_C)-1, -1, -1):
            max_idx = 0
            for j in range(1, i+1):
                if numList_C[j] > numList_C[max_idx]:
                    max_idx = j
            check = numList_C[i]
            numList_C[i] = numList_C[max_idx]
            numList_C[max_idx] = check
        return numList_C
        

def Insertion_sort(numList):
    numList_C = numList.copy()

    if N <= 10 and M <= 10:
        for i in range(1, len(numList_C)+1):
            print("L" + str(i-1)+ ": " + ' '.join(map(str,numList_C)))
            if i == len(numList_C):
                break;
            for j in range(i, 0, -1):
                if numList_C[j]<numList_C[j-1]:
                    check = numList_C[j]
                    numList_C[j] = numList_C[j-1]
                    numList_C[j-1] = check
                else:
                    break
    else:
        start = time.time()
        for i in range(1, len(numList_C)+1):
            if i == len(numList_C):
                break;
            for j in range(i, 0, -1):
                if numList_C[j]<numList_C[j-1]:
                    check = numList_C[j]
                    numList_C[j] = numList_C[j-1]
                    numList_C[j-1] = check
                else:
                    break
        
        return numList_C

if __name__ =="__main__":
    Sort(N,M)
    if N <= 10 and M <= 10:
        
        print("\n[T2] <bubble sort>")
        Bubble_sort(numList[2])
        print("\n[T2] <selection sort>")
        Selection_sort(numList[2])
        print("\n[T2] <insertion sort>")
        Insertion_sort(numList[2])
    else:
        print("\n[T2] <bubble sort>")
        get_comparison_time(Bubble_sort, copy.deepcopy(numList), True)
        print("\n[T2] <selection sort>")
        get_comparison_time(Selection_sort, copy.deepcopy(numList), True)
        print("\n[T2] <insertion sort>")
        get_comparison_time(Insertion_sort, copy.deepcopy(numList), True)