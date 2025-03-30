# Strategy-Partan
import sys
sys.stdout.reconfigure(encoding="utf-8")
from abc import ABCMeta, abstractmethod

# Strategy
class PaymentStrategy(metaclass = ABCMeta):
    @abstractmethod # このアノテーションで抽象クラスになる
    def pay(self , amount : int):
        pass
    
# Context
class ShoppingCart():
    def __init__(self):
        self.total = 0
        self.items = []
        
    def addItem(self , item : str , price : int) -> None:
        self.total += price
        self.items.append((item , price))
        
    def pay(self , paymentStrategy):
        paymentStrategy.pay(self.total)
    
# ConcreteStrategy
class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount : int):
        print(f"クレジットカードで{amount}円を支払い")

# ConcreteStrategy        
class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount : int):
        print(f"現金で{amount}円を支払い")
        
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.addItem("item1" , 500)
    cart.addItem("item2" , 1000)
    
    paymentStrategy1 = CashPaymentStrategy()
    cart.pay(paymentStrategy1)
    
    paymentStrategy2 = CreditCardPaymentStrategy()
    cart.pay(paymentStrategy2)