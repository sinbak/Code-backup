def seq_search(s, x):
    return seq_search_range( s, x, range(len(s)) ) # range(len(s))는 전체 범위

def seq_search_range(s, x, r):
    if len(r) > 0: # range의 길이(크기)가 0이상 (즉, 검색 범위가 남아있으면)
        if s[ r.start ] == x:
            return r.start
        else:
            return seq_search_range(s, x, r[1:]) # r의 가장 처음 그러니까 r.start를 제외한 나머지 범위로 재귀호출
    else: # len(r) == 0 (더 이상 검색할 범위가 없으면)
        return None

print( seq_search([1,3,2,5,4], 5) )
print( seq_search([1,3,2,5,4], 6) )
print( seq_search([1,2,2,2,5,6], 2) )


#문제1번

 
# # 아래 bin_search_range 함수를 작성하면 된다 (5점)
# def bin_search_range(ss, x, r): #ss[mid] 방식으로 푼다
#     if len(r) > 0:
#         mid = (r.start + r.stop) // 2 # None 대신에 코드 작성. (힌트: r을 이용해 mid를 계산할 수 있을 것이다) (low + high)//2 (low = 0, high = len(ss)-1)
#         if x == ss[mid]:
#             return mid
#         elif x < ss[mid]:
#             len(ss) = mid - 1
#             return bin_search_range(ss,x,range(len(ss)))
#         else:
#             r.start = mid + 1 # mid만 계산하고 나면 나머지 코드는 그렇게 어렵지 않을 것이다
#             return bin_search_range(ss,x,ss[mid:])
#     else: # len(r) == 0
#         return None # 이건 None이 리턴값이므로 그대로 둬야 함

def bin_search(ss, x):
    return bin_search_range( ss, x, range(len(ss)) )

def bin_search_range(ss, x, r): #ss[mid] 방식으로 푼다
    if len(r) > 0:
        mid = (r.start + r.stop) // 2 # None 대신에 코드 작성. (힌트: r을 이용해 mid를 계산할 수 있을 것이다) (low + high)//2 (low = 0, high = len(ss)-1)
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            return bin_search_range(ss,x,range(r.start,mid))
        else: # mid만 계산하고 나면 나머지 코드는 그렇게 어렵지 않을 것이다
            # return bin_search_range(ss,x,r[mid+1:])
            return bin_search_range(ss,x,range(mid+1,r.stop))
    else: # len(r) == 0
        return None # 이건 None이 리턴값이므로 그대로 둬야 함



print( bin_search([1,2,3,4,5], 5) )
print( bin_search([1,2,3,4,5,6], 6) )
print( bin_search([1,3,5,6], 6) )
print( bin_search([1,2,2,2,5,6], 2) )
print( bin_search([1,4,9,16,25,36,49,64,81], 81))
#문제 2번
# bsearch([1,2,2,2,3,6], 3) == range(4,5)  # 길이 1인 range 객체
# bsearch([1,2,2,2,3,6], 2) == range(1,4)  # 길이 3인 range 객체
# bsearch([1,2,2,2,3,6], 5) == range(5,5)  # 길이 0인 range 객체

# def bsearch(ss, x):
#     return bsearch_range( ss, x, range(len(ss)) )

# 아래 bsearch_range 함수를 작성하면 된다 (7점)
#range(index 범위)

# def bsearch_range(ss, x, r):
#     if len(r) > 0:
#         f, b = 0, 0
#         mid = (r.start + r.stop) // 2
#         if x == ss[mid]:
#             while x == ss[mid -f -1]:
#                 f += 1
#             while x == ss[mid +b +1]:
#                 b += 1
#             r= range(mid-f, mid+b)
#             return r
            
#         elif x < ss[mid]:
#             return bsearch_range(ss, x, range(r.start, mid))
#         else:
#             return bsearch_range(ss, x, range(r[mid+1,r.stop])) 
#     else:
#         # return bsearch_range(ss, x, range(r.stop, r.stop))
#         return r

# def bsearch(ss, x):
#     return bsearch_range( ss, x, range(len(ss)) )

# # 아래 bsearch_range 함수를 작성하면 된다 (7점)
# def bsearch_range(ss, x, r):
#     if len(r) > 0: #길이가 0보다 길 때
#         f, b = 0, 0
#         mid  = (r.start+r.stop)//2
#         if x == ss[mid]:
#             while ss[mid -1  -f] == x:
#                 f += 1
#             while ss[mid +b + 1] == x :
#                 b += 1
#             r= range(mid-f, mid+b+1)
#             return r
        
#         elif x < ss[mid]:
#             return bsearch_range(ss,x,range(r.start, mid))

#         else: #x > ss[mid]
#             return bsearch_range(ss,x, range(mid+1, r.stop))
#     else:
#         return r

# def bsearch(ss, x):
#     return bsearch_range( ss, x, range(len(ss)) )

# # 아래 bsearch_range 함수를 작성하면 된다 (7점)
# def bsearch_range(ss, x, r):
#     if len(r) > 0: #길이가 0보다 길 때
#         f, b = 0, 0
#         mid  = (r.start+r.stop)//2
#         if x == ss[mid]:
#             while ss[mid -1  -f] == x :
#                 f += 1
#             while ss[mid +b + 1] == x :
#                 b += 1
#                 if mid+ b + 1 > len(ss)-1:
#                     break
#             r= range(mid-f, mid+b+1)
#             return r

#         elif x < ss[mid]:
#             return bsearch_range(ss,x,range(r.start, mid))

#         else: #x > ss[mid]
#             return bsearch_range(ss,x, range(mid+1, r.stop))
#     else:
#         return r
def bsearch(ss, x):
    return bsearch_range( ss, x, range(len(ss)) )

# 아래 bsearch_range 함수를 작성하면 된다 (7점)
def bsearch_range(ss, x, r):
    if len(r) > 0: #길이가 0보다 길 때
        f, b = 0, 0
        mid  = (r.start+r.stop)//2
        if x == ss[mid]:
            while True:
                if ss[mid -1  -f] != x:
                    break
                if mid-1-f < 0:
                    break
                f += 1
            while True:
                if mid +b +1 >len(ss)-1:
                    break
                if ss[mid +b + 1] != x:
                    break
                b += 1
            r= range(mid-f, mid+b+1)
            return r

        elif x < ss[mid]:
            return bsearch_range(ss,x,range(r.start, mid))

        else: #x > ss[mid]
            return bsearch_range(ss,x, range(mid+1, r.stop))
    else:
        return r
    
print(bsearch([1,2,2,2,3,4], 3))
print(bsearch([1,2,2,2,3,6], 2))
print(bsearch([1,2,2,2,3,6], 5))
print(bsearch([1,2,2,3,3,4], 3))
print(bsearch([1,2,2,2,3,4], 1))
print(bsearch([1,2,2,2,2,4], 2))
print(bsearch([1,2,3,3,3,4], 3))
print(bsearch([1,2,2,2,2,3,4], 2))
#에러
print(bsearch([1,2,2,2,2,2], 2))
print(bsearch([1,2,2,2,3,4], 4))
print(bsearch([2,2,2,2,2,2], 2))