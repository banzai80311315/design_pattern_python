# Strategy-Partan
# https://qiita.com/hankehly/items/1848f2fd8e09812d1aaf

# 使いどころ
# 1.「やること」が同じで「やり方」が違う場合
# 2.物理的制限を考慮して実装する場合
# 3.メソッドの振る舞いを条件分岐で実装する場合
import sys
sys.stdout.reconfigure(encoding="utf-8")
from abc import ABCMeta, abstractmethod

class Storage(metaclass = ABCMeta):
    @abstractmethod # このアノテーションで抽象クラスになる
    def upload(self) -> None:
        pass
    
class Context():
    def __init__(self , text : str):
        self.text = text
        
    def textUpdate(self , storage : Storage) -> None:
        storage.upload(self , self.text)
        
class S3(Storage):
    def upload(self, text : str) -> None:
        print(f"{text} - をS3にuploadしました")
        
class Local(Storage):
    def upload(self, text : str) -> None:
        print(f"{text} - をLocalにuploadしました")
        
if __name__ == "__main__":
    s3 = S3()
    lo = Local()
    
    text1 = Context("すばらしい")
    text1.textUpdate(S3)