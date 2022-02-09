#package 란 module의 집합체
# import travel.thailand #모듈이나 패키지만 가능 이부분은 클래스나 함수를 직접저으로 import를 할 수가 없다
# # import travel.thailand.Thailandpackage 이렇게는 사용하지 못한다
# trip_to = travel.thailand.Thailandpackage()
# trip_to.detail()

# #단
# from travel.thailand import Thailandpackage
# trip_to = Thailandpackage()
# trip_to.detail()

# from travel import viatnam
# trip_to = viatnam.Vietnampackage()
# trip_to.detail()

#__all__

# from random import*
from travel import * #여기서 * 은 개발자가 지정하는 범위
# # trip_to = viatnam.Vietnampackage()
# trip_to = thailand.Thailandpackage()
# trip_to.detail()

#모듈 위치 확인하는 방법
import inspect #위치 파악
import random
print(inspect.getfile(random)) #random이라는 모듈이 어디에 있는지 파일정보를 알려준다
print(inspect.getfile(thailand)) #형식 : inspect.getfile(모듈명)