class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print(self):
        print(self.name + "는 " + str(self.price)+ "원 입니다.")
    def get_name(self):
        return self.name

am = Coffee("아메리카노",4100)
am.price = 5000
am.print()

es = Coffee("에스프레소", 3900)
es.name = "essprasso"
es.print()

# 클래스, 상속