# 로또 번호 생성기 만들기
# 1~45까지의 숫자를 6개 뽑기
# 1. 1~45까지의 숫자를 리스트에 생성
# 2. 리스트를 랜덤하게 만든다.
# 3. pop() 사용해서 6개를 뽑기

import random

# lotto_number = []
#
# for num in range(1, 46):
#     lotto_number.append(num)

lotto_number = [num for num in range(1,46)]

random.shuffle(lotto_number)

for i in range(6):
    print(lotto_number.pop(), end= ' ')