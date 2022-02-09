# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#     for i in new_id:
#         if i.islower() or i.isdigit() or i in ["-", "_", "."]:
#             answer += i
#     #"."는 처음과 끝에 사용할 수 없고 연속으로 사용불가능
#     while ".." in answer:
#         answer = answer.replace('..', '.')
#         print(answer)
        
#     #처음과 마지막이 .일 경우
#     if answer[0] == ".": 
#         if len(answer) >=2:
#             answer = answer[1:]
#         else:
#             answer = "."
            
#     if answer[-1] == ".":
#         answer = answer[:-1]
    
#     if answer == "":
#         answer = "a"
        
#     #아이디 길이는 3자이상 15자 이하여야한다
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == ".":
#             answer = answer[:-1]
    
#     while len(answer) < 3:
#         answer += answer[-1]
    
#     return answer

# def solution(left, right):
#     answer = 0
#     for i in range(left, right+1):
#         num_factors = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 num_factors += 1
#         if num_factors%2 == 0:
#             answer += i
#         else:
#             answer -= i
#     return answer

# def solution(s):
#     answer = s
#     n_lis = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight": 8, "nine" : 9}
#     for i in n_lis.items():
#         answer = answer.replace(i[0], str(i[1]))
#     return int(answer)

# print(solution("53threefour"))


# def solution(numbers):
#     answer = 0
#     n_sum = sum(list(range(10)))
#     answer = n_sum - sum(numbers)
#     return answer
# print(solution([1,2,3,4,6,7,8,0]))

# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i] == True:
#             answer += absolutes[i]
#         else:
#             answer -= absolutes[i]
#     return answer
# print(solution([4,7,12], [False,False,True]))

# def solution(a, b):
#     answer = 0
#     if len(a) == len(b):
#         for i in range(len(a)):
#             answer += a[i]*b[i]
#         return answer
# print(solution([1,2,3,4],[-3,-1,0,2]))
# print(solution([-1,0,1],[1,0,-1]))

# def solution(n):
#     answer = ''
#     while n > 0:			
#         n, r = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
#         answer += str(r)
#     return int(answer, 3)

# def solution(n):
#     answer = []
#     result = 0
#     while True:
#         if n < 3:
#             answer.append(n)
#             break
#         answer.append(n % 3)
#         n = n // 3
#     answer.reverse()
#     for i in range(len(answer)):
#         result += (answer[i] * (3 ** i))
#     return result

# import random
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] not in answer:
#                 answer.append(numbers[i]+ numbers[j])
#     answer.sort()
#     return answer

# def solution(a, b):
#     answer = 0
#     n_lis = [x for x in range(a,b+1)]
#     answer = sum(n_lis)
#     return answer
# def solution(n):
#     answer = []
#     for x in range(1,n+1):
#         if x%2 == 1:
#             answer.append("수")
#         else:
#             answer.append("박")
#     return ''.join(answer)
# print(solution(4))
# def solution(n):
#     n_lis = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             n_lis.append(i)
#     return sum(n_lis)
# print(solution(12))
# def solution(s):
#     if len(s) >=1 and len(s) <=5:
#         if type(s) == str:
#             s = int(s)
#     return s
# print(solution("+1234"))
# def solution(s):
#     result = []
#     for s in s.split(' '):  #띄어쓰기를 기준으로 문자를 분리해준다.
#         st = ''
#         for i in range(len(s)):  #index를 생성해주기 위해 for문을 만들어준다.
#             if i % 2 == 0:  #짝수번째라면 대문자, 홀수번째라면 소문자
#                 st += s[i].upper()  #그 결과는 st라는 새로운 공간에 붙여준다.
#             else :
#                 st += s[i].lower()
#         result.append(st)  #변형시킨 st들을 result에 리스트로 붙여준다.
#     return ' '.join(result)  #띄어쓰기를 기준으로 다시 문자를 붙여준다. 완성!   
    
# def solution(s):
#     s_lis = []
#     for s in s.split(' '):  
#         s2 = ''
#         for i in range(len(s)):
#             if i % 2 == 0:  
#                 s2 += s[i].upper()
#             else :
#                 s2 += s[i].lower()
#         s_lis.append(s2)
#     return ' '.join(s_lis)
# def solution(n):
#     n = list(str(n))
#     sum = 0
#     for i in range(len(n)):
#         sum += int(n[i])
#     return sum
# print(solution(123))
# def solution(n):
#     n = list(str(n))
#     n.reverse()
#     return list(map(int, n))
# print(solution(12345))
# def solution(n):
#     x = n**0.5
#     if x == int(x):
#         return int((x+1)**2)
#     else:
#         return -1
# print(solution(121))
# print(solution(3))
# def solution(arr):
#     answer = 0
#     arr_sum = sum(arr)
#     answer = sum(arr)/len(arr)
#     return answer

# import math
# def solution(w,h):
#     return w*h - (w+h-math.gcd(w,h))
# import random
# import math
# # def solution(numbers):

# #     numbers = list(map(str, numbers))
# #     numbers.sort(key=lambda x: x*3, reverse=True)
# #     return str(int(''.join(numbers)))

# def solution(n):
#     return str(int("".join(sorted(map(str,n),key= lambda x : (x*3),reverse = True))))

# print(solution([6,10,2]))
def solution(rows, columns, queries):

    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1,x1-1,-1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer