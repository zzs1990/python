# -*- coding: utf-8 -*-
from dataclasses import dataclass

print(f"{'-'*16}使用数据类{'-'*16}")


# Python 从 3.7 开始提供数据类功能
@dataclass
class Card:
    rank: str
    type: str


card = Card("A", "red hearts")

print(f"card == card: {card == card}")
print(f"card.rank: {card.rank}")
print(f"card.type: {card.type}")

print(f"card: {card}")

print(f"{'-'*16}使用数据类{'-'*16}")
