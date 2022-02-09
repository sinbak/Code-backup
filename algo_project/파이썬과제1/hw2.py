def merge_sort(xs, key=(lambda x: x)): #리스트를 만드는 부분
    xss = [ [x] for x in xs ] # 리스트 조건제시법 list comperehension
    [ss] = msort(xss, key)
    return ss

def msort(xss, key): # bottom-up이라 알고리즘 정의대로 작성하면 자연스럽게 꼬리재귀가 된다
    if len(xss) > 1:
        return msort( [ merge(xss[i],xss[i+1],key) if i+1 < len(xss) else xss[i]
                          for i in range(0,len(xss),2) ], key=key ) #xss의 원소들을 2개씩 merge한 리스트로 재귀호출
    else:
        return xss #len(xss) == 1안 경우 xss를 그래도 리턴

def merge(left,right, key): # 실습 5.9: merge 함수 while 버전
    ss = []
    while not (left == [] or right == []): #빈공간이 아닐 때
        # if left[0] <= right[0]:
        if min(left[0], right[0], key=key) == min(left, key=key): #왼쪽이 더 작다면 / key=key 사용하지 않을 시 error 발생
            ss.append( left[0] )  # 끝에 원소 하나 붙이기
            left = left[1:]
        else: 
            ss.append( right[0] ) # 끝에 원소 하나 붙이기
            right = right[1:]

    ss.extend(left)  # 끝에 리스트 연장 
    ss.extend(right) # 끝에 리스트 연장
    return ss
                                                                                                                                   
def func(x):
    ss2 = []
    if type(x) == int: #정수형일 때
        if (x < 0): #음수일때
            x = str(x)
            ss2.append(-ord(x[0])) #-붙이지 않을 시 1000이 200보다 먼저 정렬
            ss2.append(-len(x)) #-붙이지 않을 시 -1 -1000 -200 정렬 시 -1이 먼저 정렬이 됨
            for i in range(1, len(x)):
                 ss2.append(-ord(x[i]))
        
        else: #양수일 때
            x = "+"+str(x)
            ss2.append(-ord(x[0]))
            ss2.append(len(x))
            for i in range(1, len(x)):
                 ss2.append(ord(x[i])) 
    
    else: #정수형 제외 문자형
        for i in range(len(x)):
            ss2.append(ord(x[i]))
        # ss2.append(len(x))
    
    return ss2
# def func(x):
#     ss2 = []
#     if type(x) == str: #정수형일 때
#         for i in range(len(x)):
#             ss2.append(ord(x[i]))
#         ss2.append(len(x))
    
#     else:
#         if x < 0:
#             x = str(x)
#             ss2.append(-ord(x[0]))
#             ss2.append(-len(x))
#             for i in range(1,len(x)):
#                 ss2.append(-ord(x[i]))
#         else:
#             x = '+' + str(x)
#             ss2.append(-ord(x[0]))
#             ss2.append(len(x))
#             for i in range(1, len(x)):
#                 ss2.append(ord(x[i]))
    
#     return ss2

                
        
print(merge_sort([1,2,4,3], key=lambda x:x))
print(merge_sort([1,4,2,3], key=(lambda x: -x)))
print(merge_sort([-1,-4,2,3], key=(lambda x: -x)))
merge_sort([6,5,2,3], key=(lambda x: -x))
merge_sort([1,4,2,3], key=(lambda x: -x))
print(merge_sort([1,-1,4,3], key=lambda x:-x))
print(merge_sort([(3,'b'),(4,'a'),(1,'b'),(2,'c')],key=lambda x: (x[1], x[0])))
print(merge_sort(['apple','orange','bannana', 'beer'],key=(lambda x: ( [ ( -ord( x[i] ) ) if i < len(x) else -len(x) for i in range( len(x)+1) ] ) ) ) )
print(merge_sort([1,3,'orange',2,'bannana','apple'], key=func))
print(merge_sort([1,10000,'ace',2,'bannana','apple'], key=func))
print(merge_sort([1,-200,'linux',1000,'bannana','pine'], key=func))
print(merge_sort([-1,-200,'linux',-1000,'bannana','pine'], key=func))
print(merge_sort([-1,-200,'linux',-1000,'bannana','bannanax'], key=func))