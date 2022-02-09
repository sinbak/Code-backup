#모듈은 내가 그 모듈을 쓰려는 파일과 같은 경로 있거나 혹은 파이썬 라이버리들이 모여있는 폴더에 있어야 사용가능
# import theater_module
# theater_module.price(3) #3명이서 영화보러간 가격 
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

#2번째 방법 ( import 모듈명 as 임의로 정한 모듈명)
# import theater_module as mv
# mv.price_soldier(5)
# mv.price_morning(4)
# mv.price(3)

# #3번째 방법 ( from 모듈명 import* >>> 모듈명에 있는 모든 것을 쓰겠다는 의미)
# from theater_module import*
# price(3)
# price_morning(4)
# price_soldier(5)

#4번째 방법
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)을 쓰게 될 경우 정의되지 않았다는 에러가 뜨게 됨

from theater_module import price_soldier as price
price(5)
