# pythonは動的型付け言語
# ただし、型を使用した方がバグなどを訂正しやすくなる。version3.9以降を使用すること
# あくまで静的型付け言語ではないので型が間違っているからと言って実行ができないということはない

a: int = 1 # 整数
b: float # 浮動小数点型
c: str # 文字列
d: bool # 論理型

e: list[int] = [1,2]
f: dict[str , bool] # [Key , Value]

# 想定の値のみを定義できるLiteral
from typing import Literal
g: Literal["OK","NG"]

def sample(x: str) -> bool:
    return True