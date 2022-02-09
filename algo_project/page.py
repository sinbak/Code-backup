def getTotalPage(m,n): #m : 게시글 총 건수 n : 페이지당 보여줄 게시물 수
    if m % n ==0:
        return m //n
    else:
        return m//n + 1 # 한 페이지는 무조건 필요허기 때문에 +1

print(getTotalPage(5,10))
print(getTotalPage(10,10))
print(getTotalPage(15,10))
print(getTotalPage(30,10))

