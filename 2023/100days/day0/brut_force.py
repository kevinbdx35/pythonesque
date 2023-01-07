#Generator of all possible combinations of x digits
from string import digits
from itertools import product

#If you want to change the number of digit, input an other digit to replace 4
for passcode in product(digits, repeat=4):
    print(*passcode)
