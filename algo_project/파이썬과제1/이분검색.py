def binarySerach(lst, key):
    low = 0
    high = len(lst) - 1

    mid = (low+high) // 2    #low를 r.start   high = r.stop

    if key < lst[mid]:
        high = mid - 1  
    
    elif key == lst[mid]:
        return mid
    
    else:
        low = mid + 1


def bin_search_range(ss, x, r): #ss[mid] 방식으로 푼다
    if len(r) > 0:
        mid = (r.start + r.stop) // 2 # None 대신에 코드 작성. (힌트: r을 이용해 mid를 계산할 수 있을 것이다) (low + high)//2 (low = 0, high = len(ss)-1)
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            return bin_search_range(ss,x,range(r.start,mid))
        else: # mid만 계산하고 나면 나머지 코드는 그렇게 어렵지 않을 것이다
            return bin_search_range(ss,x,ss[mid:])
    else: # len(r) == 0
        return None # 이건 None이 리턴값이므로 그대로 둬야 함






def bsearch(ss, x):
    return bsearch_range( ss, x, range(len(ss)) )

# 아래 bsearch_range 함수를 작성하면 된다 (7점)
def bsearch_range(ss, x, r):
    if len(r) > 0:
        pass
    else:
        pass