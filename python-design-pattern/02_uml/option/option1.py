# 継承よりインターフェイス・委譲を使った方が良い理由
# https://qiita.com/yoron0122/items/d89f1b58ae376b96f42b

# NGパターン
import sys
sys.stdout.reconfigure(encoding="utf-8")
class PaymentProcessor():
    def __init__(self):
        pass
    
    def payment(self , amount : int) -> None:
        self.processPayment(amount)
        
        point = amount * (0.5/100.0)
        self._addPoint(point)
    
    def _addPoint(self , points : int) -> None:
        print(f"{points} -ポイントを付与します")
    
    def processPayment(self , amount : int) -> None:
        pass
    
    
class BarCodePayment(PaymentProcessor):
    def __init__(self):
        super().__init__()
        
    def processPayment(self , amount : int) ->None:
        print(f"{amount} -円をバーコードで支払います。")
        

class CreditCardPayment(PaymentProcessor):
    def __init__(self):
        super().__init__()
        
    def processPayment(self , amount: int )  ->None:
        print(f"{amount} -円をクレジットカードで支払います。")
        
if __name__ == "__main__":
    bar = BarCodePayment()
    cre = CreditCardPayment()
    
    print("---バーコード決済---")
    bar.payment(100)
    print("---クレジット決済---")
    cre.payment(200)