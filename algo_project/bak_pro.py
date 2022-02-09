# A = int(input())
# B = int(input())
# print(A+B)

# num,b=input().split() #입력한 문자열을 띄어쓰기로 떼어내어
# print(int(num)+int(b)) # 그 부분을 정수형으로 바꾸어 출력
# A , B = input().split()
# print(int(A) + int(B))
# print(int(A)-int(B))
# print(int(A)*int(B))
# print(int(int(A)/int(B)))
# print(int(A)%int(B))
# num,b,c = input().split()
# print((int(num)+int(b))%int(c))
# print(((int(num)%int(c))+(int(b)%int(c)))%int(c))
# print((int(num)*int(b))%int(c))
# print( ( (int(num)%int(c))*(int(b)%int(c)))%int(c))


# num = int(input())
# b = list(input())
# # print(int(num)*int(b.pop()))
# # print(num*int(b.pop()))
# # print(num*int(b.pop()))
# # print(num*int(b.pop()))
# r1 = num*int(b.pop())
# print(r1)
# r2 = num*int(b.pop())
# print(r2)
# r3 = num*int(b.pop())
# print(r3)
# print(r1+10*r2+100*r3) #3자리수 한정

# N = int(input())
# for i in range(1,10):
#     print("{0} * {1} = {2}".format(N,i,N*i))

# num, b = input().split()

# if int(num) > int(b):
#     print(">")
# elif int(num) < int(b):
#     print("<")
# elif int(num) == int(b):
#     print("==")

# score = input()
# if 90<= int(score) <=100:
#     print("A")
# elif 80<= int(score) <=89:
#     print("B")
# elif 70<= int(score) <=79:
#     print("C")
# elif 60 <= int(score) <=69:
#     print("D")
# else:
#     print("F")

# year = input()
# if int(year)%4 == 0 and int(year)%100 != 0 or int(year)%400 ==0:
#     print(1)
# else:
#     print(0)

# x = input()
# y = input()
# if int(x)>0 and int(y)>0:
#     print(1)
# elif int(x)>0 and int(y) <0:
#     print(4)
# elif int(x) <0 and int(y)<0:
#     print(3)
# elif int(x)<0 and int(y)>0:
#     print(2)
# else:
#     print()

# H, M = input().split()
# if int(M) < 45 and int(H)>0:
#     print(int(H)-1, 60-(45-int(M)))
# elif int(H) == 0:
#         print(23, 60-(45-int(M)))

# elif int(M) >= 45:
#     print(int(H), int(M)-45)

# H, M = map(int,input().split())
# if M < 45:
#     if H == 0:
#         print(23, 60-(45-M))
#     else:
#         print(H-1, 60-(45-M))
# else:
#     print(H, M-45)

# N = int(input())
# sum = 0
# for i in range(1,N+1):
#     sum += i
# print(sum) #>> 들여쓰기 잘할 것

# import sys

# # T=int(input())
# T = int(sys.stdin.readline()) 
# for i in range(int(T)):
#     num,b = map(int,sys.stdin.readline().split()) # input을 사용하는 대신 sys 모듈을 import하여 대체한다(빠른 A+B )
#     print(num+b)
    
# x = input()
# for i in range(int(x)):
#     i = i+1
#     num,b = map(int, input().split())
#     print("Case #{0}: {1}".format(i, (num+b)))

# x = input()
# for i in range(int(x)):
#     i = i+1 
#     num,b = map(int, input().split())
#     print("Case #{0}: {1} + {2} = {3}".format(i,num,b,(num+b)))

# N = int(input())
# for i in range(int(N)):
#     i +=1
#     print("*"*i) 
# for i in range(int(N)):
# for i in range(int(N)):
#     for j in range(int(N)):
#         if i > j:
#             print(" ", end= " ")
#         else:
#             print("*", end = " ")
#     print()
        
# for i in range(int(N)+1):
#     print(" "*(int(N)-i)+"*"*i) 
 
# x = input()
# for i in range(1, int(x)+1): #줄 수
#     for j in range(int(x)-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end = " ")
# N = input()
# for i in range(int(N)):
#     A,B = map(int, input().split())
#     print(A+B)


# while True:
#     A,B = map(int, input().split())
#     if A ==0 and B ==0:
#         break
    # print(A+B)


# while True:
#     try:
#         A,B = map(int, input().split())
#         print(A+B)
#     except:
#         break

# N = num = int(input())
# count  = 0
# while True:
#     t= N // 10 #몫(십의 자리)
#     o = N % 10 #나머지(일의 자리)
#     p = t + o # 각 자리의 합
#     count = count + 1 #횟수
#     N = int(str(N%10)+str(p%10)) 
#     if(num == N):
#         break
# print(count)

# N = int(input())
# l = list(map(int, input().split()))
# print(min(l), max(l))
    
# l = list(map(int, input().split()))
# M = max(l)
# print(M)
# print(l.index(M)+1)

# l = [] #빈 리스트 선언
# for i in range(9): #9개의 숫자
#     l.append(int(input())) #리스트에 추가

# print(max(l))
# print(l.index(max(l))+1)

# l = []
# for i in range(3): # 3개의 수
#     l.append(int(input())) #리스트에 추가
# num = l[0] #1번
# b = l[1] #2번
# c = l[2] #3번
# p = num*b*c
# numult = list(str(p))
# for i in range(10):
#     print(numult.count(str(i)))
    
# l = []
# for i in range(10):
#     l.append(int(input())%42)
# l = set(l)
# print(len(l))


# l = []
# for i in range(10):
#     N = int(input())
#     l.append(N % 42)
# l = set(l)
# print(len(l))

# c = int(input())
# score = list(map(int, input().split()))
# M = max(score) #최댓값

# for i in range(c):
#     score[i] = score[i]/M*100
#     average = sum(score)/c
# print("%.2f" %average)
# 3333333333333333333333333333333333333333333333333333
# N = int(input()) #횟수 입력
# for i in range(N):
#     num = input() # 입력
#     l = list(num) #리스트에 요소 추가
#     sum  = 0 #O가 연속할 시 점수계산
#     sc = 1
#     for i in l: #리스트에서 반복
#         if i == "O": #요소가 O일 때
#             sum += sc #합에 +1 / 
#             sc += 1 #점수에 +1
#         else:
#             sc = 1 #연속 O가 아닐 때
#     print(sum)

# N = int(input()) 
# for i in range(N): #횟수
#     s_lis = list(map(int, input().split()))
#     avg = sum(s_lis[1:])/s_lis[0]
#     count = 0
#     for score in s_lis[1:]:
#         if score > avg:
#             count += 1 #평균 이상인 학생 수
#     rate = count/s_lis[0]*100
#     print(f"{rate:.3f}%") #f-string 기법
#     #{}를 이용하여 변수를 삽입할 수 있다

# def solve(n_list):
#     sum = 0
#     for i in n_list:
#         sum += i
#     return sum

#첫번째 방법
# def d(N): #d()함수 선언
#     num = 0 #처음 값
#     for i in list(str(N)):
#         num = num + int(i)
#         return int(i) + num #전번 + 현재
# num = [] #리스트로 변환
# for j in range(1,10001): #리스트에 반복
#     r = d(j)
#     num.append(r) #num 리스트에 요소 더하기

# for K in range(1, 10001): #결과값을 반복해서 출력
#     if K in num:
#         pass
#     else:
#         print(K)

# num = set(range(1,10001)) #숫자범위 설정
# generated_num = set() #빈 공간
# for i in range(1,10001): 
#     for j in str(i): #셀프넘버(1 + 1, 3+3)
#         i += int(j) #차례대로 더하기
#     generated_num.add(i) # 빈 공간에 대입
# self_num = num - generated_num #generated_num에 포함된 부분을 제외
# for K in sorted(self_num): #남은 부분에서 반복
#     print(K)

# N = int(input())
# H = 0 #한수
# for i in range(1, N+1):
#     if i < 100:
#         H += 1
#     else:
#         l = list(map(int, str(i)))
#         if l[0] - l[1] == l[1]-l[2]:
#             H += 1
# print(H)
# anything = input()
# print(ord(anything))
# ===================================
# N = int(input()) #횟수
# p = list(input()) #리스트에 들어갈 내용
# numult = 0 #결과값

# for i in p: #리스트 내용 내
#     numult += int(i) 
# print(numult) 
# =====================================
# A = input() #입력할 값
# index = list(range(ord("num"), ord("z")))
# for i in index:
#     print(int(A.find(chr(i))),end= " ")
# import sys
# N = int(sys.stdin.readline())

# for x in range(N):
#     count,string=sys.stdin.readline().split()
#     count = int(count)
#     string = str(string)
#     for y in range(count):
#         print(count*string[y], end = " ")
#     print() #줄 내림
# #import sys 이용해보기

# # N = int(input())
# # for i in range(N):
# #     C, S = input().split()
# #     for j in range(len(S)):
# #         print(S[j]*int(P), end='')
# #     print()

# N = int(input())

# for i in range(N):
#     c, p = input().split()
#     for x in p:
#         print(x*int(c), end=" ") 
#     print()  # 줄넘김

# import sys
# N = int(sys.stdin.readline())
 
# for i in range(N):
#     c, p = sys.stdin.readline().split()
 
#     for j in p:
#         for K in range(int(c)):
#             print(j, end=" ")
 
#     print("")

# T = int(input())
# for i in range(T):
#     R, S = input().split()
#     R = int(R)
#     S = list(S)
#     for j in range(len(S)):
#         print(S[j]*R, end='')
#     print()

# st = input().upper() #대문자로 적용 AAAABB
# st_list = list(set(st)) # A B
# l = [] #빈 리스트
# for i in st_list:
#     count = st.count(i) #개수 구하기
#     l.append(count) #구한 개수를 리스트로 정리

# if l.count(max(l)) >= 2: #최대인 문자가 2개 이상일때
#     print("?")
# else:
#     print(st_list[(l.index(max(l)))])

# word = list(input().split())
# print(len(word))

# n1, n2 = input().split()
# l1 = list(n1)
# l2 = list(n2)
# l1.reverse()
# l2.reverse()
# sum1 = int(l1[0])*100 + int(l1[1])*10 + int(l1[2])
# sum2 = int(l2[0])*100 + int(l2[1])*10 + int(l2[2])
# if sum1 > sum2:
#     print(sum1)
# elif sum2 > sum1:
    # print(sum2)

#1 / 2: ABC / 3: DEF/ 4: GHI / 5: JKL / 
# 6: MNO / 7: PQRS / 8: TUV / 9: WXYZ 
# num_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] 
# n_ring = input() #문자 입력
# sum = 0 #총 걸리는 시간
# for alpabet in num_list: #리스트에 있는 알파벳들 ABC DEF ...
#     for i in alpabet: #num_list[i] 에 있는 알파벳들 EX) ABC
#         for j in n_ring: #친 알파벳들
#             if j == i: #두 알파벳이 같다면
#                 sum += num_list.index(alpabet) + 3 #다이얼에서 알파벳은 핀에서부터 3초
# print(sum)

#크로아티아 알파벳
# cro_list = ['c=','c-','dz=','d-','lj','nj','p=','z=']
# IN = input()
# # count = 0
# for word in cro_list: #리스트 내
#     IN = IN.replace(word, '1')
# print(len(IN))

#그룹단어체커
#같은 문자는 연속해서 출연해야 그룹
# 1번 방법
# N = int(input()) #횟수
# # leteral = list(input())
# count = 0 #그룹단어 수
# for i in range(N):
#     leteral = input()
#     count2 = 0
#     for j in range(len(leteral)-1):
#         if leteral[j] != leteral[j+1]:
#             leteral_list = leteral[j+1:]
#             if leteral_list.count(leteral[j])>0:
#                 count2 += 1
#     if count2 == 0:
#         count += 1
# print(count)

#2번 방법
# num = int(input())
# wood = 0
# for i in range(num):
#     word = input()
#     for j in range(len(word)):
#         if j != len(word)-1:
#             if word[j] == word[j+1]:
#                 pass
#             else:
#                 if word[j] in word[j+1]:
#                     wood += 1
# print(wood)

# N = int(input()) #횟수
# count=0
# for i in range(N):
#     num = list(map(str,input()))
#     b=[] #이미 나온 문자
#     for j in range(len(num)) :
#         if num[j] == num[0] :
#             b.append(num[j])
#         elif num[j] != num[0] :
#             if  num[j] in b : 
#                 break
#             else:
#                 num[0] = num[j]
#                 b.append(num[j])
#         if j+1 == len(num) : #단일문자 해결
#             count+=1
# print(count)

# N = int(input()) #목표지점
# first = 1 #시작할 때의 방 개수
# plus = 6 #추가 1/ 2~7(6) / 8~19(12) ...
# room = 1 # 방 개수
# if N == 1: #시작
#     print(1)
# else:
#     while True:
#         first = first + plus #2~7(6) 방2개/8~19(12)방3개
#         room+= 1
#         if N <= first:
#             print(room) #방 개수를 출력
#             break
#         plus += 6 #등처수열

# number = int(input())
# add1 = number//10
# add2 = number%10
# line = 1 #분자(줄 수와 일치)
# under = 1
# if number > 10:
#     for i in range(add1):
#         line += 1   
#     for j in range(add2):
#         under += 1
#     print(f"{line}/{under-1}")
# # print("{0}/{1}".format(line, under))
# # print(line,"/",under)
# elif number <= 10:
#     for j in range(add2):
#         under += 1
#     print(f"{line}/{under-1}")
# 1/1 1/2 2/1 3/1 2/2 
# number = int(input())
# line = 1
# under = 1
# for i in range(number):
    
#==================================
#달팽이
# import sys
# import math
# A, B, V = map(int, sys.stdin.readline().split())
# # day_wood = (V-B)/(A-B)
# day_wood2 = (V-A)/(A-B)
# # print(math.ceil(day_wood))
# print(math.ceil(day_wood2)+1)

# person = int(input()) #횟수
# for i in range(person):
#     h,w,N = map(int, input().split()) #층/호수/몇번째 인원
#     add1 = N%h #층 증가
#     add2 = N//h #호수 증가
#     floor = 0 #층
#     r_number = 0 #호수
#     if add1 == 0:
#         floor = h*100
#         r_number = add2
#     else:
#         floor = add1*100
#         r_number = 1 + add2
#     print(floor+r_number)

# A = input() #입력할 값
# index = list(range(ord("num"), 123))
# # print(ord("num")) #97
# # print(ord('z')) #122
# for i in index:
#     print(A.find(chr(i)),end= " ")

# t = int(input()) #Test case 수

# for _ in range(t):  
#     floor = int(input())  # 층(K)
#     num = int(input())  # 호(N)
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for K in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ N-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력 -1 마지막 첫번 째을 의미

# T = int(input()) #Test case 수

# for _ in range(T):

#     K = int(input()) #층
#     N = int(input()) #호
#     people = [ i for i in range(1, N+1)]  # 1 ~ N-1까지 (인덱스로 사용)

#     for __ in range(K):
#         for j in range(1,N):
#             people[j] += people[j-1] # 층별 각 호실의 사람 수를 변경 #0층 :1234 1층:1 3 6 10...

#     print(people[-1])

# sugar = int(input())
# sum = 0
# while sugar >= 0:
#     if sugar%5 == 0:
#         sum += (sugar//5) 
#         print(sum)
#         break
#     sugar -=3 #5의배수가 될 때까지 -3
#     sum += 1 #sum 에 개수가 1씩 증가
# else:
#     print(-1) #위 방식을 반복해서 음수가 된 경우 -1 출력

# import sys

# A, B = map(int, sys.stdin.readline().split())
# print(A+B)

# Count = int(input()) #횟수
# for i in range(Count):
#     x,y = map(int, input().split())
#     distance = y - x
#     num = 0
#     move = 1 #num별 이동가능한 거리
#     move_sum = 0 #이동한 거리의 합
#     while move_sum < distance:
#         num += 1
#         move_sum += move #num 에 해당하는 move를 더함
#         if num % 2 == 0: #2의 배수일 때
#             move += 1
#     print(num)

# num_list = int(input()) #횟수
# wood = 0
# so = list(map(int, input().split()))
# if num_list == len(so): #입력한 횟수와 so의 길이가 같은 경우
#     for i in so:
#         if i != 1:
#             for j in range(2,i):
#                 if (i/j) % 1 == 0:

# N을 입력받는다.
# N = int(input())

# # N회만큼 자연수를 입력받는다. ==>> 여기서 질문!!
# num_list = list(map(int, input().split()))

# count = 0
# for num in num_list:
#     # 자연수가 1이라면
#     if num == 1: 
#         continue
#     # 자연수가 1이 아니라면
#     else:
#         # 2부터 그 자연수보다 1작은 수까지 약수가 있다면 빠져나오고
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         # 그렇지 않다면 count에 1을 더하고 빠져나온다.
#         else:
#             count += 1
# print(count)

# M = int(input()) #두 수를 입력
# N = int(input())
# sosu_lis = []
# for num in range(M, N+1):
#     err = 0 
#     if num > 1: #1보다 클 때
#         for i in range(2,num):
#             if num % i == 0:
#                 err += 1
#                 break
#         if err == 0:
#             sosu_lis.append(num)
# if len(sosu_lis) != 0:
#     print(sum(sosu_lis))
#     print(min(sosu_lis))
# else:
#     print(-1)

# start_num = int(input())
# last_num = int(input())

# sosu_list = []
# for num in range(start_num, last_num+1):
#     error = 0
#     if num > 1 :
#         for i in range(2, num):  # 2부터 num-1까지
#             if num % i == 0:
#                 error += 1
#                 break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
#         if error == 0:
#             sosu_list.append(num)  # error가 없으면 소수리스트에 추가
            
# if len(sosu_list) > 0 :
#     print(sum(sosu_list))
#     print(min(sosu_list))
# else:
#     print(-1)
# import sys
# import math
# M , N = map(int, sys.stdin.readline().split())
# sosu_lis = []
# for num in range(M, N+1):
#     err = 0
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 err += 1
#                 break
#         if err == 0:
#             sosu_lis.append(num)
# if len(sosu_lis) != 0:
#     for x in sosu_lis:
#         print(x)

# M , N = map(int, sys.stdin.readline().split())
# sosu_lis = []
# for num in range(M, N+1):
#     err = 0
#     if num > 1:
#         for i in range(2,int(num**0.5)+1):
#             if num % i == 0:
#                 err += 1
#                 break
#         if err == 0:
#             sosu_lis.append(num)
# if len(sosu_lis) != 0:
#     for x in sosu_lis:
#         print(x)
# def find_sosu(num):
#     if num <= 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
# M , N = map(int, input().split())

# for i in range(M,N+1):
#     if find_sosu(i):
#         print(i)



# M, N = list(map(int, input().split(' ')))
# def is_prime(num):
#     if(num <= 1):
#         return False
    
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             return False
        
#         i += 1
#     return True

# for i in range(M, N + 1):
#     if(is_prime(i)):
#         print(i)

# f = int(input())
# def factorial(f):
#     if f == 0:
#         return 1
#     elif f == 1:
#         return 1
#     return f*factorial(f-1)

# print(factorial(f))

# p = int(input())
# def Fibonacci(p):
#     if p == 0:
#         return 0
#     elif p == 1:
#         return 1
#     return Fibonacci(p-1)+Fibonacci(p-2)

# print(Fibonacci(p))

# star = int(input())

# def stars(N):
#     matrix=[] #리스트 이용
#     for i in range(3*len(N)):
#         if i // len(N) == 1: #위치가 1인 경우 (위치는 0,1,2 ... 순)
#             matrix.append(N[i%len(N)]+ " "*len(N) + N[i % len(N)])
#         else:
#             matrix.append(N[i% len(N)] * 3)
#     return (list(matrix))

# model = ["***", "* *", "***"]
# N = int(input())
# x = 0
# while N != 3:
#     N = int(N/3) #3으로 나눈 나머지
#     x += 1

# for i in range(x):
#     model = stars(model)
# for i in model:
#     print(i)

# def concatenate(r1, r2):
#     return [''.join(x) for x in zip(r1, r2, r1)]
 
# def star10(N):
#     if N == 1:
#         return ['*']
#     N //= 3
#     x = star10(N)
#     num = concatenate(x, x)
#     b = concatenate(x, [' '*N]*N)
 
#     return num + b + num
 
# print('\N'.join(star10(int(input())))) #join >> 리스트에서 문자열로

# import random
# N, M= map(int, input().split())
# # N = int(input())
# for i in range(N):
#     print(random.randrange())

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# numult = 0 #합
# for i in range(N):
#     for j in range(i+1,N):
#         for K in range(j+1, N):
#             if arr[i] + arr[j] + arr[K] > M: #부른 값보다 크다면
#                 continue
#             else: #M 보다 작거나 같은 최댓값 구하기
#                 numult = max(numult, arr[i] + arr[j] + arr[K]) #큰 값을 출력
# print(numult)
# import sys
# N = sys.stdin.readline
# l = []
# for i in range(int(N())):
#     l.append(int(N()))

# l = sorted(l)
# for i in l:
#     print(i)

# N = int(sys.stdin.readline()) #횟수
# arr = [int(sys.stdin.readline()) for i in range(N)]
# sys.stdout.write("\N".join(map(str, sorted(arr)))) #sys.stdout.write(개행을 제거하고 출력)
#sorted 만 쓰면 str 형식이야지 map 형식은 아니라고 뜬다
# N = int(sys.stdin.readline()) #횟수
# arr = [int(sys.stdin.readline()) for i in range(N)]
# for i in sorted(arr):
#     print(i)
# import sys
# N = int(sys.stdin.readline())
# # num_list = []
# numult_list = [0 for _ in range(10001)]
# for i in range(N):
#     numult_list[int(sys.stdin.readline())] += 1 #크기 10000의 1차원 배열을 만들고 숫자를 받을 때마다 해당 인덱스 값을 1씩 늘린다

# for i in range(len(numult_list)):
#     for j in range(numult_list[i]):
#         print(i)
# #https://developmentdiary.tistory.com/280 참고

# C = int(input())
# stage, num = 1, 1 #초기
# while stage + num <= C: #입력한 값보다 작거나 같을 때
#     num += stage #num 변수에 stage 값을 누적하며 어느 스테이지에 있는지 검사
#     stage += 1 #스테이지 증가
# row = C - num #열
# x, y = row + 1, stage - row

# # 1. stage 값이 홀수일 때 : 분자는 1부터 증가, 분모는 stage 값부터 감소

# # 2. stage 값이 짝수일 때 : 분자는 stage 값부터 감소, 분모는 stage 1부터 증가

# if stage % 2 == 0:
#     print("{}/{}".format(x,y))
# else:
#     print("{}/{}".format(y,x))


# word_wood = int(input())
# word_list = list()
# sorted_list = list()
# for _ in range(word_wood):
#     word_list.append(input())

# set_word = set(word_list) #중복제거
# for word in set_word:
#     sorted_list.append((len(word), word))

# sorted_list.sort() # 길이와 사전 순
# for word_len, word in sorted_list: #2가지를 반복하여 한 후
#     print(word) #단어만 출력을 한다

# num = int(input()) #인원수
# member = list()
# for _ in range(num):
#     age, name = map(str, input().split())
#     age = int(age)
#     member.append((age, name))
# member.sort(key = lambda member: (member[0]))

# for i in range(num):
#     print(member[i][0], member[i][1])

# N = int(input()) #입력할 횟수
# loc = list()
# for _ in range(N):
#     x, y = map(int, input().split())
#     loc.append((x,y))
# loc.sort(key= lambda loc: (loc[0]))
# loc.sort(key= lambda loc: (loc[1]))
# for i in range(N):
#     print(loc[i][0], loc[i][1])
# import sys
# N = int(sys.stdin.readline())

# location = [] #좌표
# for _ in range(N):
#     (x,y) = list(map(int,sys.stdin.readline().split()))
#     location.append((x,y))
# location_sorted = sorted(location)
# for i in location_sorted:
#     print(i[0], i[1])

#hanoi
# N = int(input())
# def hanoi(N,start,last,assist):#start:시작지점/ last: 목표지점 /assit : 보조지점
#     if N == 1:
#         print(start,last)  # 원반 한 개를 옮기는 문제면 그냥 옮기기
#         return
#     hanoi(N-1,start,assist,last) #판 N-1개를 보조로 이동
#     print(start, last) #가장 큰 판을 목표지점으로 이동
#     hanoi(N-1,assist,last,start) #보조에 있는 판 N-1을 목표지점으로 옮기기
# count = 1
# for i in range(N-1):
#     count = count*2+1
# print(count)
# hanoi(N,1,3,2)

# print('''\\    /\\''')
# print(''' )  ( ')''')
# print('''(  /  )''')
# print(''' \\(__)|''')

# print("|\_/|")
# print("|d p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\__|")
# N = int(input()) #숫자 입력
# numult = 0
# for i in range(1, N+1):
#     num_list = list(map(int, str(i))) #str함수를 통해 i의 각 자리수를 리스트에 넣기
#     numult = i + sum(num_list) # 원래 숫자 i 와 각 자리 숫자의 합을 더한다
#     if numult == N: #입력값과 sum 값이 같은 경우
#         print(i)
#         break
#     if i == N: #생성자가 없는 경우
#         print(0)

# global M #원하는 길이
# def NandM(arr1, arr2):
#     if len(arr2)==M: #만약 M 개를 골라졌을 경우
#         for i in range(M):
#             print(arr2[i],end=" ")
#         print() #줄바꿈
#         return
#     else: #만약 M개가 골라졌지 않았을 경우
#         for i in range(len(arr1)): 
#             if arr1[i] not in arr2: #arr1의 요소가 arr2에 없다면
#                 arr2.append(arr1[i]) #arr2에 추가(배열에 숫자추가)
#                 for j in range(len(arr2)):
#                     NandM(arr1,arr2) #위에 있는 코드로 이동
#                 arr2.pop() #맨 뒤의 숫자를 뺴주면서 바뀌는 걸 반복

# N,M = map(int, input().split())
# arr1=[i+1 for i in range(N)] #1~N 의 수
# arr2 = [] #빈 리스트
# NandM(arr1,arr2)

# def DFS(index,p):
#     if index==M:
#         for x in num:
#             print(x,end=' ')
#         print()
#     else:
#         for i in range(p,N+1):
#             num[index] = i #num에 숫자를 대입
#             DFS(index+1,i+1)

# N,M=map(int,input().split())
# num=[0]*M #M 만큼 리스트 확장
# DFS(0,1)

# def dfs(index):
#     if index == M:
#         for x in num:
#             print(x, end = ' ')
#         print()
#     else:
#         for i in range(1, N+1):
#             num[index] = i
#             dfs(index+1)

# N, M = map(int, input().split())
# num = [0]*M
# dfs(0)

# def DFS(index):
#     if index==M:
#         for x in num:
#             print(x,end=' ')
#         print()
#     else:
#         for i in range(1,N+1):
#             if l[i]==0:
#                 l[i]=1
#                 num[index]=i
#                 DFS(index+1)
#                 l[i]=0 #백 트래킹 다시 위로 돌아가기!(값 되돌리기)

# N,M=map(int,input().split())
# l=[0]*(N+1) #+1을 해주지 않으면 out of range 에러가 뜸(숫자 범위가 1~ N) 중복체크하는 리스트
# num=[0]*M #한 줄에 들어가는 숫자 수
# DFS(0)
# # N, M = map(int, input().split())
# # num_lis = [0 for _ in range(N+1)]
# # count = [0 for _ in range(M)]

# import sys

# # 정수 X를 스택에 넣는 연산이다.
# def push(x):
#     stack.append(x)

# # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# def pop():
#     if(not stack):
#         return -1
#     else:
#         return stack.pop()

# # 스택에 들어있는 정수의 개수를 출력한다.
# def size():
#     return len(stack)

# # 스택이 비어있으면 1, 아니면 0을 출력한다.
# def empty():
#     return 0 if stack else 1

# # 스택의 가장 위에 있는 정수를 출력한다. 
# # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# def top():
#     return stack[-1] if stack else -1

# N = int(sys.stdin.readline().rstrip())
# stack = []

# for _ in range(N):
#     input_split = sys.stdin.readline().rstrip().split() #rstrip : 오른쪽에서 제거

#     order = input_split[0]

#     if order == "push":
#         push(input_split[1])
#     elif order == "pop":
#         print(pop())
#     elif order == "size":
#         print(size())
#     elif order == "empty":
#         print(empty())
#     elif order == "top":
#         print(top())

# import sys
# from collections import deque
# N = int(sys.stdin.readline())
# d = deque([])
# for i in range(N):
#     p = sys.stdin.readline().split()
#     if p[0] == 'push':
#         d.append(p[1])
#     elif p[0] == 'pop':
#         if not d:
#             print(-1)
#         else:
#             print(d.popleft())
#     elif p[0] == 'size':
#         print(len(d))
#     elif p[0] == 'empty':
#         if not d:
#             print(1)
#         else:
#             print(0)
#     elif p[0] == 'front':
#         if not d:
#             print(-1)
#         else:
#             print(d[0])
#     elif p[0] == 'back':
#         if not d:
#             print(-1)
#         else:
#             print(d[-1])




    
# N = int(input())
# print_num = 0
# for i in range(1, N+1):
#     div_num = list(map(int, str(i)))
#     sum_num = i + sum(div_num)
#     if(sum_num == N):
#         print_num = i
#         break
# print(print_num)

# import sys
# N, M = map(int, sys.stdin.readline().split())
# Num_list = [i+1 for i in range(N)]

# def is_palindrome(word):
#     # 코드를 입력하세요.
#     l = list(word)
#     for i in range(len(l)//2):
#         if l[i] == l[-i-1]:
#             continue
#         else:
#             return False
#     return True


            

# # 테스트
# print(is_palindrome("racecar"))
# print(is_palindrome("stars"))
# print(is_palindrome("토마토"))
# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))

# import sys
# N = int(sys.stdin.readline())

# stack = list()

# for i in range(N):
#     cmd = sys.stdin.readline().split()

#     if cmd[0] == "push":
#         stack.append(int(cmd[1]))

#     elif cmd[0] == "pop":
#         if not stack:
#             print(-1)
#         else:
#             print(stack[-1])
#             stack.pop()

#     elif cmd[0] == "size":
#         print(len(stack))

#     elif cmd[0] == "empty":
#         if not stack:
#             print(1)
#         else:
#             print(0)

#     elif cmd[0] == "top":
#         if not stack:
#             print(-1)
#         else:
#             print(stack[-1])

# N = int(input())
# n_list = list(map(int, input().split()))

# M = int(input())
# m_list = list(map( int, input().split()))

# for i in range(len(m_list)):
#     if m_list[i] in n_list:
#         print(1)
#     else:
#         print(0)

# import sys
# input = sys.stdin.readline
# N = int(input())
# p = list(map(int, input().split()))
# M = int(input())
# s_ = list(map(int, input().split()))
# p.sort()
# for i in s_:
#     low, high = 0, N
#     while low <= high:
#         mid = (low + high) // 2
#         if mid < N and mid > -1:
#             if p[mid] < i: low = mid + 1
#             else: high = mid - 1
#         else: 
#             break
#     if mid < N and mid > -1:
#         if i == p[high + 1]: print(1)
#         else: print(0)
#     else: print(0)

# count = int(input())
# n_call = []
# for i in range(count):
#     num = int(input())
#     if num == 0:
#         n_call.pop()
#     else:
#         n_call.append(num)
# print(sum(n_call))

# num = int(input())
# for i in range(num):
#     source_bracket = input()
#     bracket = list(source_bracket) #문자열로 받아 리스트로 만든다
#     sum = 0
#     for i in bracket:
#         if i == '(': # ( 가 나올 시 sum에 +1
#             sum += 1
#         elif i == ')': # ) 가 나오면 sum 에 -1
#             sum -= 1
#         if sum < 0: 
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

# while True:
#     p = input()
#     if p == '.':
#         break
#     stack = []
#     bool = True
#     for i in p:
#         if i == '(' or i == '[':
#             stack.append(i)
#         elif i == ')':
#             if not stack or stack[-1] == '[':
#                 bool = False
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#         elif i == ']':
#             if not stack or stack[-1] == '(':
#                 bool = False
#                 break
#             elif stack[-1] == '[':
#                 stack.pop()
#     if bool == True and not stack:
#         print('yes')
#     else:
#         print('no')

# N = int(input())
# p = []
# p2 = []
# count = 1
# bool = True #수열 가능 여부
# for i in range(N): #8
#     num = int(input())
#     while count <= num:
#         p.append(count)
#         p2.append('+')
#         count += 1
#     if p[-1] == num:
#         p.pop()
#         p2.append('-')
#     else:
#         bool = False
# if bool == False:
#     print('NO')
# else:
#     for i in p2:
#         print(i)

# N = int(input())
# stack = [] #숫자들
# re_stack = [] #결과 +, -
# count = 0
# bool = True #수열 가능 여부

# for _ in range(N):
#     num = int( input())
#     while count < num:
#         count += 1
#         stack.append(count)
#         re_stack.append("+")
#     if stack[-1] == num:
#         stack.pop()
#         re_stack.append("-")
#     else:
#         bool = False
#         break

# if bool == False:
#     print("NO")
# else:
#     for i in re_stack:
#         print(i)


# numbers = int(input())
# num_list = list(map(int, input().split()))
# stack = []
# result = [-1 for _ in range(numbers)]

# for i in range(len(num_list)):
#     try:
#         while num_list[stack[-1]] < num_list[i]:
#             result[stack.pop()] = num_list[i]
#     except:
#         pass
        
#     stack.append(i)
        
# for i in range(numbers):
#     print(result[i], end = ' ')

# import sys
# N= int(input())
# num = list(map(int,sys.stdin.readline().split()))
# for i in range(len(num)):
#     lay = []
#     for j in num[i+1:]:
#         if j > num[i]:
#             lay.append(j)
#     if lay:
#         print(lay[0],end=' ')
#     else:
#         print(-1,end=' ')

# import sys
# N = int(input())
# num = list(map(int, input().split()))
# NEG = [ -1 for _ in range(N)]
# i = 1
# stack = []
# stack.append(0)
# while stack and i < N:
#     while stack and num[stack[-1]] < num[i]:
#         NEG[stack[-1]] = num[i]
#         stack.pop()
#     stack.append(i)
#     i += 1

# for i in NEG:
#     print(i, end=" ")

# N = int(input())
# arr = list(map(int, input().split()))
# stack = []
# answer = [-1]*N
# for i in range(N):
#     while stack and stack[-1][0] < arr[i]:
#         val, index = stack.pop()
#         answer[index] = arr[i]

#     stack.append((arr[i], i))

# for ans in answer:
#     print(ans, end=' ')
# import sys
# from collections import deque
# N = int(sys.stdin.readline())
# d = deque([])
# for i in range(N):
#     s = sys.stdin.readline().split()
#     if s[0] == 'push':
#         d.append(s[1])
#     elif s[0] == 'pop':
#         if not d:
#             print(-1)
#         else:
#             print(d.popleft())
#     elif s[0] == 'size':
#         print(len(d))
#     elif s[0] == 'empty':
#         if not d:
#             print(1)
#         else:
#             print(0)
#     elif s[0] == 'front':
#         if not d:
#             print(-1)
#         else:
#             print(d[0])
#     elif s[0] == 'back':
#         if not d:
#             print(-1)
#         else:
#             print(d[-1])

# import sys
# a = int(sys.stdin.readline())
# N = [i for i in range(1, a+1)]

# while len(N) > 1: # 리스트에 요소가 하나만 남을 때까지
#     N.pop(0)
#     N.append(N[0])
#     N.pop(0)

# print(N[0])

# from collections import deque
# num = int(input())
# deque = deque([i for i in range(1, num +1)])

# while len(deque) != 1:   
#     deque.popleft()
#     deque.rotate(-1)

# print(deque[0])

# N, K = map(int, input().split())
# de = [i for i in range(1,N+1)]
# print("<",end='')
# i = 0

# while len(de) > 1:
#     i = i+K
#     if i > len(de):
#         i = i % len(de)
#         if i == 0:
#             i = i+ len(de)
#     i = i-1
#     print(str(de.pop(i)), end=", ")

# print("{}>".format(str(de.pop())))



# N = int(input())  
# for _ in range(N):
#     N, M = map(int,input().split())

#     num_list = list(map(int,input().split()))
#     check = [0 for _ in range(N)] #0으로 구성된 리스트 생성
#     check[M] = 1 # 궁금한 문서위치 저장
# #N : 문서의 개수 / M : 큐에 몇 번째에 놓여있는지 나타내는 정수
#     count=0 #순번
#     while True: #참인 동안
#         if num_list[0] == max(num_list): #첫번째가 우선순위가 가장 높을 때 / max 메소드를 이용하여 중요도 리스트의 최댓값
#             count+=1 #순번 뒤로

#             if check[0] != 1: #1이 아니라면
#                 del num_list[0]
#                 del check[0]
#             else:
#                 print(count)
#                 break
#         else:
#             num_list.append(num_list[0])
#             check.append(check[0])
#             del num_list[0]
#             del check[0]

# import sys
# input = sys.stdin.readline
# a,b,c,d,e,f = map(int,input().split())

# for i in range(-999,1000):
#     for j in range(-999,1000):
#         if a * i + b * j == c and d * i + e * j == f:
#             print(i, j)

# import sys
# input = sys.stdin.readline

# N = int(input())
# apple = list(map(int, input().split()))
# all_apple = sum(apple)
# turn = all_apple // 3

# if all_apple % 3 != 0: #3으로 나눈 나머지가 0이 아닌 경우
#     print('NO')
# else:
#     for a in apple:
#         turn -= (a//2)
#     if turn > 0:
#         print('NO')
#     else:
#         print('YES')
# #모든 사과나무 리스트를 돌면서 2로 나눈 몫의 총 합이 전체합 //3 보다 커야 가능한 사과나무들의 높이
# #모든 사과나무의 합이 9이므로 3의 배수이고, 전체 합의 //3 이 3이므로, 각 사과나무에 할당되는 +2의 개수가 총 3개여야 한다.
# # 그런데 높이가 1인 사과나무에 +2를 할당할 수 없고, 높이가 3인 사과나무에 +2를 2개이상 할당할 수 없으므로, 전체 +2는 두번밖에 할 수가 없다.

# N, M = map(int, input().split())
# lay = [input() for _ in range(N)]
# wood = 0 
# for i in range(N): #행
#     j = 0 #열
#     while j < M:
#         if lay[i][j] == '|':
#             j += 1
#         else:
#             wood += 1
#             while j < M and lay[i][j] == '-':
#                 j += 1
# for j in range(M): #열
#     i = 0 #행
#     while i < N:
#         if lay[i][j] == '-':
#             i += 1
#         else:
#             wood += 1
#             while i < N and lay[i][j] == '|':
#                 i += 1
# print(wood)
# #행과 열을 검사한다.

# import sys

# N = int(sys.stdin.readline())
# linkArr = [0] * N
# edges = []
# # 링크 수를 arr에 담고, edges를 채운다.
# for _ in range(N - 1):
#     a, b = map(int, sys.stdin.readline().split(" ")) #node 번호
#     linkArr[a - 1] += 1
#     linkArr[b - 1] += 1
#     edges.append([a, b])
# treeD, treeG = 0, 0
# # 조합을 이용하여 ㅈ트리를 구한다.
# for i in range(N):
#     treeG += linkArr[i] * (linkArr[i] - 1) * (linkArr[i] - 2) / 6 if linkArr[i] >= 3 else 0
# # 두 노드의 link 수를 이용하여 ㄷ트리를 구한다.
# for a, b in edges:
#     treeD += (linkArr[a - 1] - 1) * (linkArr[b - 1] - 1)
# if treeD > treeG * 3:
#     print("D")
# elif treeD < treeG * 3:
#     print("G")
# else:
#     print("DUDUDUNGA") #DFS(깊이탐색)을 이용한 방식 -> 문제해결을 위해서는 넓이탐색으로 풀어야한다


# import sys
# read = sys.stdin.readline

# def comb(a, b):
#     ans = 1
#     if a-b < b:
#         b = a-b
#     for i in range(a-b+1, a+1): #조합
#         ans *= i
#     for j in range(1, b+1):
#         ans //=j
#     return ans

# N = int(read())
# edge = []
# degree = [0 for _ in range(N+1)]

# for _ in range(N-1):
#     a, b = map(int, read().split())
#     edge.append([a, b])
#     degree[a] += 1
#     degree[b] += 1

# du = 0 #D 그래프
# ga = 0 # G 그래프

# for e in edge:
#     temp = (degree[e[0]]-1) * (degree[e[1]]-1)
#     du += temp

# for idx in range(1, N+1):
#     if degree[idx] >= 3:
#         ga += comb(degree[idx], 3)

# #print(du, ga)

# if du > 3 * ga:
#     print('D')
# elif du < 3 * ga:
#     print('G')
# else:
#     print('DUDUDUNGA')

import sys
read = sys.stdin.readline
N = int(read())
tree = [ [] for i in range(N+1)]

for i in range(N-1):
    a, b= list(map(int, input().split()))
    tree[a].append(b) #서로 연결
    tree[b].append(a)

start = [1] #시작
done = [0 for i in range(N+1)] #방문한 곳인지 확인
result = {} #result[4] 는 4번 노드의 부모가 담긴다.

while start:
    pos = start.pop(0)
    for i in tree[pos]:
        if done[i] == 0: #방문한 적이 없다면
            result[i] = pos
            done[i] = 1 #방문했으므로 1로 바꾸기
            start.append(i) #다음 탬색 진행

for i in range(2, N+1):
    print(result[i])


# import sys
# V = int(sys.stdin.readline())
# tree = [[] for _ in range(V+1)]
# for _ in range(V):
#     path = list(map(int, sys.stdin.readline().split()))
#     len_path = len(path)
#     for i in range(1, len_path//2):



import sys
v = int(sys.stdin.readline())
node_graph = [[] for _ in range(v+1)]
for i in range(v):
    path = list(map(int, sys.stdin.readline().split()))

    # 각 입력 Line의 정보를 받아 Parsing 후 node_graph에 연결 정보 저장
    path_len = len(path)
    for i in range(1, path_len//2):
        node_graph[path[0]].append([path[2*i-1], path[2*i]])

# 첫 번째 DFS 결과
result_first = [0 for _ in range(v+1)]

def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start]+d
            DFS(e, matrix, result)

DFS(1, node_graph, result_first) # 아무 노드에서 시작해준다
result_first[1] = 0 # 루트 노드가 정해져 있지 않아 양방향으로 입력을 받기 때문에 해당

tmpmax = 0 # 최댓값 구하기
index = 0 # 최장경로 노드

for i in range(len(result_first)):
    if tmpmax < result_first[i]:
        tmpmax = result_first[i]
        index = i

# 최장경로 노드에서 다시 DFS를 통해 트리의 지름을 구함
result_final = [0 for _ in range(v+1)]
DFS(index, node_graph, result_final)
result_final[index] = 0
print(max(result_final))

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1, 2):
        Tree[temp[0]].append((temp[i], temp[i+1]))
print(Tree)


def bfs(index):
    visit = [-1] * (N+1)
    q = deque([index])
    visit[index] = 0
    Max = [0, 0]

    while q:
        print(q)
        old = q.popleft()
        print(q)
        for i in Tree[old]:
            if visit[i[0]] == -1:
                visit[i[0]] = visit[old] + i[1]
                q.append(i[0])
                if Max[0] < visit[i[0]]:
                    Max[0] = visit[i[0]]
                    Max[1] = i[0]
        print(Max)
        print(visit)
    return Max

value, f_node = bfs(1)
print("**")
print(f_node)
answer, e_node2 = bfs(f_node)
print(answer, e_node2)
print(answer)


from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n)]
    c[x] = 0
    while q:
        x = q.popleft()
        for w, nx in a[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

n = int(input())
a = [[] for _ in range(n)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    a[x-1].append([w, y-1])
    a[y-1].append([w, x-1])
print(bfs(bfs(0, 1), 2))

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):  # 중위 순회
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):  # 후위 순회
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])

import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
zero = 0 #흰색
first = 0 #파랑

def slice(x, y, n):
    global zero, first
    complete = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if complete != paper[i][j]:
                slice(x, y, n//2)
                slice(x, y+n//2, n//2)
                slice(x+n//2, y, n//2)
                slice(x+n//2, y+n//2, n//2)
                return

    if complete == 0:
        zero += 1
        return

    else:
        first += 1
        return

slice(0,0,n)
print(zero)
print(first)


N = int(input())

block = [list(map(int, input())) for _ in range(N)]

def quad(x, y, n):
    # n = 1, 하나의 픽셀만 볼 경우,
    if(n == 1):
        return str(block[x][y])
    
    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(block[i][j] != block[x][y]):
                result.append('(')
                result.extend(quad(x, y, n//2))
                result.extend(quad(x, y + n//2, n//2))
                result.extend(quad(x + n//2, y, n//2))
                result.extend(quad(x + n//2, y + n//2, n//2))
                result.append(')')
                return result
            
    return str(block[x][y])
    
print(''.join(quad(0, 0, N)))

import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0 # -1
result1 = 0 # 0
result2 = 0 # 1

def slice(x,y,n):
    global result, result1, result2
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        slice(x+n//3*a. y+n//3*b, n//3)
                return

    if check == -1:
        result += 1
    elif check == 0:
        result1 += 1
    elif check == 1:
        result2 += 1

slice(0,0,n)
print(result1)
print(result2)

def power(a, b):
    if b == 1: 
        return a % C
    else:
        temp = power(a, b // 2) 
        if b % 2 == 0:
            return temp * temp % C 
        else:
            return temp * temp * a % C 


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)

import sys
a, b, c = map(int, sys.stdin.readline().split())

def div(x, y):
    if y == 1:
        return x% c
    result = div(x, y//2)

    if y%2 == 0:
        return result*result% c
    
    else:
        return result*result * x % c
print(div(a,b))

s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
first = 0
second = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            first = s[i]
            second = s[j]
s.remove(first)
s.remove(second)
s.sort()
for i in s:
    print(i)


E,S,M,cnt =1,1,1,1

cnt_E , cnt_S , cnt_M = map(int,input().split())

while(True):
    if cnt_E==E and cnt_S==S and cnt_M==M :
        break
    E+=1 ; S+=1 ; M+=1; cnt+=1
    if E>=16 : E-=15
    if S>=29 : S-=28
    if M>=20 : M-=19

print(cnt)

T = int(input())
def plus(n):
    if n == 1:
        return 1
    elif n ==2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus(n-1) + plus(n-2) + plus(n-3)

for i in range(T):
    n = int(input())
    print(plus(n))

import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
x = 0
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()
print(-1)

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def next_permutations(a) :
    i=len(a)-1
    while i > 0 and a[i-1] >= a[i] :
        i-=1
    if i<=0 :
        return False
    
    j=len(a)-1
    while a[i-1] >= a[j] :
        j-=1
    a[i-1],a[j] = a[j],a[i-1]

    j=len(a)-1 
    while i < j :
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1

    return True

n=int(input())
a=list(map(int,input().split()))

if next_permutations(a) :
    print(' '.join(map(str,a)))
else :
    print(-1)