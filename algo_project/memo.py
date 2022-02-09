import sys
option = sys.argv[1] #첫번째 인자
memo = sys.argv[2]

# print(option)
# print(memo)

if option == "-a":
    f = open('memo.txt', 'a')

#python memo.py -a "Life is too short"