class Espresso:
    def __init__(self):
        self.price = 3900

    def make(self):
        print("원두를 갈아 넣습니다.")
        print("에스프레소를 추출합니다.")

    def print(self):
        print("가격은 "+str(self.price)+ " 원 입니다.")

#
# es2 = Espresso()
# es2.make()
# es2.print()