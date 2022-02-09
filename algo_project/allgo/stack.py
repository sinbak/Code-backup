# def push(n):
#     lst.append(n)

# def pop():
#     try:
#         print(lst.pop())
#     except:
#         print(-1)

# def size():
#     return len(lst)

# def empty():
#     num = 1 if size() ==0 else 0 #size 0이라면 1 아니면 0
#     print(num)

# def top():
#     try:
#         print(lst[-1]) #맨 오른쪽 출력
#     except:
#         print(-1) #-1 출력
    
# num = int(input())
# lst = []
# for _ in range(num):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         push(cmd[1])
#     elif cmd[0] == 'pop':
#         pop()
#     elif cmd[0] == 'size':
#         print(size())
#     elif cmd[0] == 'empty':
#         empty()
#     elif cmd[0] == 'top':
#         top()

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# import sys
# N = int(sys.stdin.readline())

# stack = list()

# for i in range(N):
#     cmd = sys.stdin.readline().split()

#     if cmd[0] == "push":
#         stack.append(int(cmd[1]))

#     elif cmd[0] == "pop":
#         if not stack:
#             print('-1')
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

# count = int(input())
# num_call = []
# for i in range(count):
#     num = int(input())
#     if num == 0: #0을 선언 시 가장 최근 숫자를 뺀다
#         num_call.pop()
#     else: #나머지는 추가
#         num_call.append(num)
# print(sum(num_call))

# count = int(input())
# def bracket(count):
#     for i in range(count+1):
#         vps = list(input())
#         stack = []
#         for j in range(len(vps)):
#             if vps[0] == ')' or vps[-1] == '(':
#                 return 'No'
#             elif vps[(0)] == '(' and vps[-1] == ')' and vps.count('(') == vps.count(')'):
#                 return 'Yes'
# for _ in range(count):
#     print(bracket(count))   

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
def coin_pay(coin, m):
    if m > 0:
        while len(coin) > 0 and m < coin[0]:
            coin = coin[1:]   # 지불 금액보다 더 큰 단위의 동전 제외
        if coin[0] > 1: 
            n1 = coin_pay(coin[1:], m)   # None대신 coins[0] 동전을 사용하지 않고 지불하는 경우 최소 코인 개수를 구하는 식 작성 함수 m값이 변하지 않는다
            count1 = n1[0]
            dic1 = n1[1].copy()
            #n1[0] 총 최소 코인 개수
            n2 = coin_pay(coin, m - coin[0]) #튜플 (2,{5:1,1:1})
            count2 = n2[0]+1 # copy_did = {n2[1]} # copy_did = coin[0]+= 1
            dic2 = n2[1].copy()
            if coin[0] in dic2:
              dic2[coin[0]] += 1
            else:
              dic2[coin[0]] = 1

            #n2[0] 총 최소 코인 개수
            if count1 < count2:
              return (count1, dict(sorted(dic1.items(), reverse=True)))
            else:
              return (count2, dict(sorted(dic2.items(), reverse=True)))

        else: # coins[0] == 1
            return (m,{1:m}) # 총 m개의 동전이 필요하며 1짜리 동전 m개 사용해 지불
       
    else: # m == 0
        return (0,{}) # 지불해야 할 금액이 0으로 없으므로 필요한 동전도 0개고 함께 빈 map을 타나태는 {}를 리턴