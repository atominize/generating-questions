# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import bino1
import mult1
import mult2
from utils import multi_coefficient
from binomialTheorem import BinomialTheorem

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(multi_coefficient(5,[2, 1, 2]))
    # print(mult2.test())
    x = BinomialTheorem("x", 2, "y", -4, 3)
    print(x.expansion())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
