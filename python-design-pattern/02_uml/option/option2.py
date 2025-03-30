# 仕様変更が発生
# 「バーコード決済の場合のみポイントを付加率を1%」

# option1についてだと、親クラスのロジック変更になってしまいクレジット決済に対しても影響が出てしまう。
# ⇒では、paymentメソッドもオーバーライドするか？？
# ⇒それはそれで、ポイント付加のロジック以外は全く同じ処理になって重複する
# ⇒そして、今後決済手法が増えるなどしてしまうとそれに対してpaymentをオーバーライドしなくては行けなくて大変
# !! 親クラスとほぼ同じコードが、具象クラス側で増殖しいていく !!

# また、最悪の場合親クラスに条件分岐をつけることも・・・
# 一件解決していそうだが、そうなると決済方法が増えるたびに抽象クラスを見直す必要が出てくる。

# リファクタリング1:インターフェイスの追加
import sys
from abc import ABCMeta, abstractmethod
from numpy import double
sys.stdout.reconfigure(encoding="utf-8")

class PaymentStrategy(metaclass = ABCMeta):
    @abstractmethod # このアノテーションで抽象クラスになる
    def processPayment(self , amount : int) -> None:
        pass
    
    @abstractmethod # このアノテーションで抽象クラスになる
    def getPointRate(self) -> double:
        pass

class PaymentProcessor():
    def __init__(self , paymentStrategy : PaymentStrategy):
        self.__paymentStrategy = paymentStrategy
        
    def payment(self , amount : int) -> None:
        ## インターフェイスを実装したクラスに対応した決済を行う
        self.__paymentStrategy.processPayment(amount)
        
        ## インターフェイスを実装したクラスに対応したポイント付与を行う
        point = amount * self.__paymentStrategy.getPointRate()
        self._addPoints(point)
    
    def _addPoints(self , points : int) -> None:
        print(f"{points}-ポイントを付与しました。")
    
class BarCodePaymentStrategy(PaymentStrategy):
    def processPayment(self, amount) -> None:
        print(f"{amount} - 円をバーコード決済します「")
    
    def getPointRate(self) -> double:
        return 1.0 / 100.0
    
class CreditCardPaymentStrategy(PaymentStrategy):
    def processPayment(self, amount) -> None:
        print(f"{amount} - 円をクレジットカード決済します「")
    
    def getPointRate(self) -> double:
        return 0.5 / 100.0
    
if __name__ == "__main__":
    bar = BarCodePaymentStrategy()
    cre = CreditCardPaymentStrategy()
    
    acount1 = PaymentProcessor(bar)
    acount2 = PaymentProcessor(cre)
    
    print("---バーコード決済---")
    acount1.payment(1000)
    print("---クレジット決済---")
    acount2.payment(1000)
    
# この内容はoption3.pyのStrategyパターンとなる。