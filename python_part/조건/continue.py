absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue #스킵하고 계속 진행
    elif student in no_book:
        print("오늘수업은 여기까지. {0}은 교무실로!".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0: #나머지가 0인 경우
            print(n, 'equals', x, '*',n//x)
            break  #조건을 만족할 시 종료
        else:
            print(n, 'is prime number')

for n in range(2,10):
    if n%2 == 0:
        print("even")
    else:
        print("odd")
    
        
