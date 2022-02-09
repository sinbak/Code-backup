import sys
import random
#과제 1번
N, M = map(int,sys.stdin.readline().split())
numList = []
test = []
def Sort(N,M):
    if N<= 10 and M <= 10: #출력 조건
        for i in range(N):
            x = int(input())
            numList.append(x)
            numList.sort()
        for j in range(M):
            if j == 0:
                print("T"+ str(j)+": " + ' '.join(map(str,numList)))
            elif j == 1:
                numList.reverse() 
                print("T"+ str(j)+": " + ' '.join(map(str,numList)))
            else:
                random.shuffle(numList)
                print("T"+ str(j)+": " +' '.join(map(str,numList)))
    else:
        print("{} test case inputs generated.".format(M))
        print("{} integers in each test case.".format(N))

def Bubble_sort(numList):
    print()
    print("[T2] <bubble sort>")
    for i in range(len(numList)):
        print("L" + str(i)+ ": " + ' '.join(map(str,numList)))
        for j in range(len(numList)-i-1):
            if numList[j]>numList[j+1]:
                temp=numList[j+1]
                numList[j+1]=numList[j]
                numList[j]=temp


def Insertion_sort(numList):
    for i in range(0, len(numList)):
        print("L" + str(i)+ ": " + ' '.join(map(str,numList)))
        for j in range(i, 0 ,-1):
            if numList[j]<numList[j-1]:
                check=numList[j]
                numList[j] = numList[j-1]
                numList[j-1] = check
            else:
                break

def Selection_sort(numList):
        min_index = 0
        for i in range(len(numList)):
            print(numList)
            min_index = i
            for j in range(i+1, len(numList)):
                if numList[min_index] > numList[j]:
                    min_index = j
            temp = numList[min_index]
            numList[min_index]= numList[i]
            numList[i] = temp


if __name__ =="__main__":
    Sort(N,M)
    
    Bubble_sort(numList)
    # numList = numList
    # Insertion_sort(numList)
    # Selection_sort(numList)
    # print("L" + str(i)+": "+ ' '.join(map(str, numList)))
#버블, 선택, 삽입
# def bubble_sort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def insertion_sort(arr):
#     for end in range(1, len(arr)):
#         for i in range(end, 0, -1):
#             if arr[i - 1] > arr[i]:
#                 arr[i - 1], arr[i] = arr[i], arr[i - 1]



# numList = []
# for i in range(N):
#     x = int(sys.stdin.readline())
#     numList.append(x)
#     for j in range(M):
#         if j == 0:
#             sorted(numList)
#         elif j == 1:
#             print( reversed(numList))
#         else:
#             print( random.shuffle(numList))

#푸는 방법
# numList= ["numList","b","c", "d", "e"]
# for i in range(5):
#     if i == 0:
#         print("T"+ str(i)+": " + ' '.join(sorted(numList)))
#     elif i == 1:
#         print("T"+ str(i)+": " +" ".join(reversed(numList)))
#     else:
#         random.shuffle(numList)
#         print("T"+ str(i)+": " +' '.join(numList))

# T = int(input())
# for t in range(1, T+1):
#     abc = input()
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#     result = []
#     count = 0
#     while count<10:
#         if count & 1:
#             result.append(num_list.pop(0))
#         else:
#             result.append(num_list.pop())
#         count+=1
#     print("#{} ".format(t), end='')
#     print(*result)
