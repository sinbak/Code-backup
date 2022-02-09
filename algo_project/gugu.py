# def gugu(s):
#     result = []
#     i = 1
#     for i in range(1,10):
#         result.append(s*i)
#         i +=1
#     return result
# print(gugu(2))

# A = int(input())
# B = int(input())
# print(A+B)

# a,b=input().split() #입력한 문자열을 띄어쓰기로 떼어내어
# print(int(a)+int(b)) # 그 부분을 정수형으로 바꾸어 출력
# A , B = input().split()
# print(int(A) + int(B))
# print(int(A)-int(B))
# print(int(A)*int(B))
# print(int(int(A)/int(B)))
# print(int(A)%int(B))
# a,b,c = input().split()
# print((int(a)+int(b))%int(c))
# print(((int(a)%int(c))+(int(b)%int(c)))%int(c))
# print((int(a)*int(b))%int(c))
# print( ( (int(a)%int(c))*(int(b)%int(c)))%int(c))

def solution(n): 
    answer = 0
    n = list(str(n)) 
    for i in n:
        answer += int(i)
    return answer

print(solution(987)) #24
print(solution(123)) #6
