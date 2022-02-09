def exists_in(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

def exists_in_rec(arr, target):
    x = 0
    if len(arr) == 0 :
        return False
    else:
        if arr[x] == target:
            return True
        
        return exists_in_rec(arr[x+1:], target)

def compare(func1, func2, *args):
    ret1 = func1(*args)
    ret2 = func2(*args)
    print(f"{func1.__name__}=>{ret1}")
    print(f"{func2.__name__}=>{ret2}")
    print(f"equal?={ret1==ret2}")
    print()
#--------------------------------------------- 1번 ^

def sum_n_to_m(n, m):
    ret_val = 0
    for i in range(n, m+1):
        ret_val += i
    return ret_val

def sum_n_to_m_rec(n, m):
    if n <= m:
        return n + sum_n_to_m_rec(n+1, m)
    else:
        return 0
#----------------------------------------- 2번 ^

def concat_rec(left, right):
    result = left[:]
    if len(right) > 0:
        result.append(right[0])
        return concat_rec(result, right[1:])
    return result
#----------------------------------------- 3번 ^

def shooting_rec2(distance_left, count):
    if distance_left < 0.01:
        print(count)
    else:
        shooting_rec2(distance_left/2.0, count+1)


def shooting_iter(distance_left):
    count = 0
    while distance_left >= 0.01:
        distance_left = distance_left/2.0
        count += 1
    print(count)
shooting_iter(10)
shooting_iter(5)
shooting_iter(1)
#----------------------------------------- 4번 ^