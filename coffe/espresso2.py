class Espresso:
  count = 0

  def __init__(self):
      self.price = 3900
      Espresso.count += 1

  def get_price(self):
      print("가격은 " + str(self.price) + "원 입니다.")

  @staticmethod
  def sale_count():
      print("에스프레소가 " + str(Espresso.count) + "개 팔렸습니다.")

espresso = Espresso()
Espresso.sale_count()