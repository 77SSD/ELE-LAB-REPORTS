#eecode.py
import string

def to_decimal(num_str, base):
    decimal = 0
    power = 0
    for i in range(len(num_str) - 1, -1, -1):
        if num_str[i].isdigit():
            decimal += int(num_str[i]) * base ** power
        else:
            decimal += (ord(num_str[i].lower()) - ord('a') + 10) * base ** power
        power += 1
    return decimal

def from_decimal(decimal, base):
    result = ''
    while decimal > 0:
        digit = decimal % base
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(digit - 10 + ord('A')) + result
        decimal //= base
    return result

def convert_base(num_str, base1, base2):
    decimal = to_decimal(num_str, base1)
    return from_decimal(decimal, base2)

if __name__ == '__main__':
    num_str = input("Enter the string number: ")
    base1 = int(input("Enter the input base: "))
    base2 = int(input("Enter the output base: "))
    result = convert_base(num_str, base1, base2)
    print(f"{num_str} in base {base1} is {result} in base {base2}")