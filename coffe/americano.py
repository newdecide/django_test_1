# class Americano:
#     def __init__(self):
#         self.price = 4100
#
#     def make(self):
#         print("원두를 갈아 넣습니다.")
#         print("원두를 추출합니다.")
#         print("물을 추가 합니다.")
#
#     def print(self):
#         print("가격은 " + str(self.price) + " 원 입니다.")


from coffe.espresso import Espresso

class Americano(Espresso):
    def __init__(self):
        super().__init__()
        self.price += 200

    def make(self):
        super().make()
        print("물을 추가 합니다.")

    def __str__(self):
        return "아메리카노 클래스입니다."

am = Americano()
am.make()
am.print()