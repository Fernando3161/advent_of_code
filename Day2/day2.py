
import os
import pandas as pd


class Submarine(object):
    horiz = 0
    depth = 0
    aim = 0
    product = 0

    def __init__(self) -> None:
        super().__init__()

    def move(self, direction, amount):
        if direction == "forward":
            self.horiz += amount

        elif direction == "down":
            self.depth += amount

        elif direction == "up":
            self.depth -= amount

    def move_corrected(self, direction, amount):
        if direction == "forward":
            self.horiz += amount
            self.depth += amount*self.aim

        elif direction == "down":
            self.aim += amount

        elif direction == "up":
            self.aim -= amount

    @property
    def product(self):
        return self.depth*self.horiz


df = pd.read_csv(
    os.path.join(os.getcwd(), "Day2", "inputd2.txt"),
    header=None, names=["dir", "amount"], sep=" ")

sub = Submarine()
for x, y in zip(df["dir"], df["amount"]):
    sub.move(x, y)
print(sub.product)

sub2 = Submarine()
for x, y in zip(df["dir"], df["amount"]):
    sub2.move_corrected(x, y)
print(sub2.product)
