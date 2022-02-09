from bisect import bisect, insort
# import networkx as nx
# from matplotlib import pyplot as plt
# data = [215, 320, 609, 714]
# index = bisect(data, 400)
# print(index)
# data.insert(index, 400)
# print(data)
# insort(data, 700)
# print(data)
# def bisect_right(a,x,lo=0,hi=None):
#     if lo<0:
#         raise ValueError('lo must be non-negative')
#     if hi is None:
#         hi = len(a)
#     while lo < hi:
#         mid = (lo+hi)//2
#         if x < a[mid]:
#             hi = mid
#         else:
#             lo = mid+1
#     return lo
# V = {0, 1, 2, 3, 4}
# N = len(V)
# E = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 4)}
# # E |= {(y, x) for (x, y) in E}
# G = (V, E) # 가중치 없는 무향 그래프
# adjList = {v:[] for v in V}
# # 여기에 작성
# for x,y in E:
#     adjList[x].append(y)
#     adjList[y].append(x)
#     print();print(x,y)
# for v in V: 
#     print(v, '->', adjList[v])

# def dfs(v):
#     visited.add(v)
#     print(v)
#     for w in adjList[v]:
#         if w not in visited:
#             print(v, "->", w)
#             dfs(w)
# visited = set()
# dfs(0)

# V = {1, 2, 3, 4, 5}
# E ={(1, 2), (1, 3), (1, 4), (2, 3), 
# (2, 5), (3, 5), (4, 5)}
# G = (V, E)
# L = {v:[] for v in V}
# for x,y in E:
#     L[x].append(y)
#     L[y].append(x)
#     print(x,y)
# for v in V:
#     print(v,"-",L[v])
# def dfs(x):
#     for i in l[x]:
#         if visited[i] == False:
#             print(x, i, sep = " - ")
#             visited[i] = True
#             dfs(i)

# v = {1, 2, 3, 4, 5}
# e = {(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 5), (4, 5)}
# g = (v, e)

# l = {i : [] for i in v}
# for x, y in e:
#     l[x].append(y)
#     l[y].append(x)

# visited = [True] + [True] + [False] * (len(v) - 1)
# dfs(1)
V = {1, 2, 3, 4, 5}
E = {(1, 2):3, (1, 3):6, (1, 4):3, (2, 3):1, 
(2, 5):5, (3, 5):2, (4, 5):5}
E.update({(y, x): E[(x, y)] for (x, y) in E})
WEIGHT_MAX = 1000
G = (V, E)
L = {v:set() for v in V}
for x, y in E:
    L[x].add(y)
    L[y].add(x)

def extractMin(Q,D): #D:  가중치 Q: 지나간 노드?
    pass

def prim(s): #초기화
    D = {v: WEIGHT_MAX for v in V}
    D[s] = 0
    S = set()
    # print(D)
    while S != V:
        u = extractMin(V-S, D)
        S.add(u)
    return sum(D.values()) 
print('(prim) MST =', prim(1))


