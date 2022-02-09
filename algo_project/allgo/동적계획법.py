# # N = int(input())
# # for _ in N:
# #     A, B = map(int, input().split())


# # #[1,3,2,4,6,10,9,7]
# # #[8,9,2,1,4,10,7,6]

# # N = int(input())
# # weightireList = [ list(map(int, input().split())) for  in range(N)]
# # print(weightireList)

# #LCS
# L = list(input().upper())
# C = list(input().upper())
# L_len = len(L)
# C_len = len(C)
# dp = [ [ 0 ] * (C_len+1) for i in range(L_len+1)] #2차원배열생성
# for i in range(L_len):
#     for j in range(C_len): #반복문을 통해 각 문자 비교
#         if L [i ] == C[ j ]: #문자가 같을 시
#             dp[ i+1 ][ j+1 ] = dp[ i ][ j ] + 1 #1씩 추가
#         else: #같지 않다면
#             dp[ i+1 ][ j+1 ] = max(dp [ i+1 ][ j ], dp [ i ][ j+1 ] ) #큰값을 대입

# print( dp[ L_len ][ C_len ] ) #마지막 값 출력

# #1012
# t = int( input( ) )
# movaluee_y = [ -1, 1, 0, 0 ] #상하 좌우
# movaluee_x = [ 0, 0, -1, 1 ] #상하 좌우
# field =  [ [ 0 ] * 50 for i in range(51)] #2500 공간할당

# for _ in range(t):
#     M, N, K = map(int, input().split())


# #백준 1012 정답
# # from collections import deque
 
# # tc = int(input())
# # dx = [-1, 1, 0, 0]
# # dy = [0, 0, -1, 1]
 
# # for i in range(tc):
# #     N, M, k = map(int, input().split())
# #     graph = [[0] * M for _ in range(N)]
# #     for _ in range(k):
# #         a, b = map(int, input().split())
# #         graph[a][b] = 1
    
# #     def bfs(graph, xPos, yPos):
# #         q = deque()
# #         q.append((xPos, yPos))
# #         graph[xPos][yPos] = 2
# #         weighthile q:
# #             x, y = q.popleft()
# #             for i in range(4):
# #                 nx = x + dx[i]
# #                 ny = y + dy[i]
# #                 if 0 <= nx < N and 0 <= ny < M:
# #                     if graph[nx][ny] == 1:
# #                         q.append((nx, ny))
# #                         graph[nx][ny] = 2
# #     count = 0
# #     for i in range(N):
# #         for j in range(M):
# #             if graph[ i ][ j ] == 1:
# #                 bfs(graph, i, j)
# #                 count += 1
# #     print(count)
# # #1912
# # N = int(input()) #n개의 정수
# # lis = list(map(int, input().split())) #숫자들 입력

# # dp = [ x for x in lis ]

# # for i in range(1, N):
# #     dp[ i ] = max(dp[ i ], dp[ i - 1 ] + lis[ i ])

# # print(max(dp))

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# N = int(input())

# def check(x, y):
#     key = y*M+x
#     if key in d:
#         return 0
#     else:
#         d[key] = 1
#         if arr[y][x] == 0:
#             return 0
#     if x < M-1:
#         check(x+1, y)
#     if y < N-1:
#         check(x, y+1)
#     if x > 0:
#         check(x-1, y)
#     if y > 0:
#         check(x, y-1)
#     return 1

# cnt = 0
# for i in range(N):
#     M, N, k = map(int, input().split(' '))
#     arr = [[0 for _ in range(M)] for _ in range(N)]
#     d = dict()
#     cnt = 0
#     for i in range(k):
#         x, y = map(int, input().split(' '))
#         arr[y][x] = 1
#     for i in range(N):
#         for j in range(M):
#             cnt += check(j, i)
# print(cnt)

# import sys
# sys.setsqrursionlimit(10*9)

# def search(roweight,col):
#     if ((0 <= roweight) and (roweight < N)) and ((0 <= col) and (col < M)):
#         if(Baechu[roweight][col] == 1):
#             Baechu[roweight][col] = -1
#             search(roweight,col-1)   # 왼쪽
#             search(roweight,col+1)   # 오른쪽
#             search(roweight-1,col)   # 위
#             search(roweight+1,col)   # 아래
 
# # if name == "main":

# #     Test_case = int(input())

# #     for i in range(Test_case):
# #         M, N, K = map(int,input().split())
# #         Baechu = [[0]M for _ in range(N)]
# #         Count = 0

# #         for j in range(K):
# #             x,y = map(int,input().split())
# #             Baechu[y][x] = 1

# #         for roweight in range(N):
# #             for col in range(M):
# #                 if Baechu[roweight][col] > 0:
# #                     search(roweight,col)
# #                     Count += 1

# #         print(Count)


#1051 문제
size = 1 #크기가 1인 정사각형
N,M = map(int,input().split())  #행 : N 열 : M
sqr = [ list(input()) for _ in range(N) ]
for i in range(N-1):
    for j in range(M-1):
        num = sqr[ i ][ j ]
        for k in range( i+1,N ):
            if sqr[ k ][ j ] == num:
                len = k - i
                if j + len < M :
                    if (sqr[ i ][ j + len ] == num) and (sqr[ i + len ][ j + len ]==num ):
                        size = max(size,len+1)
                
print(size**2)

# 12865
import sys

input = sys.stdin.readline
# 물건 개수, 버틸 수 있는 무게
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)] # 무게별 최대 가치 저장소

# 모든 물건에 대해서 확인
for i in range(1, n + 1):
    # 무게, 가치
    weight, value = map(int, input().split())
    # 무게별 확인
    for j in range(1, k + 1):
        # 현재 물건의 무게가 가방 무게 j보다 무거운 경우
        if weight > j:
            dp[i][j] = dp[i - 1][j]  # 전에 물건 결과값 가져오기
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])
# =============================================
N, K = map(int,input().split())
pd = [[0,0]]
dp = [[[0,0] for j in range(N+1)] for i in range(N+1)]

for i in range(N):
    weight, value = map(int,input().split())
    pd.append([weight,value])

for i in range(1,N+1):
    for j in range(i,N+1):
        weighteight = dp[i][j-1][0] + pd[j][0]
        valuealue = dp[i][j-1][1] + pd[j][1]
        if(weighteight <= K):
            dp[i][j] = [weighteight,valuealue]
        else:
            dp[i][j] = max(dp[i][j-1], pd[j])

Max = 0
for i in range(N+1):
    for j in range(N+1):
        if (dp[i][j][1] > Max):
            Max = dp[i][j][1]

print(Max)