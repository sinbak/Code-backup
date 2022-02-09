#에러가 일어났을 때 그에 대해서 처리해주는 것

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 문자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 문자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하셨습니다.")
# except ZeroDivisionError as err:
#     print(err)


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 문자를 입력하세요 : ")))
    nums.append(int(input("두 번째 문자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하셨습니다.")
except ZeroDivisionError as err:
    print(err)
except: #위에 있는 에러경우를 제외한 모든 에러를 여기서 처리
    print("알 수 없는 에러가 발생하였습니다")
# except Exception as err:
#     print(err) >> 이런 식으로 에러의 정확한 내용을 알 수 있다