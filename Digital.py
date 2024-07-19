# Taking binary input
if binary = input("Enter a binary number:")
# Calling the function
   BinaryToDecimal(binary)
def BinaryToDecimal(binary):
 decimal = 0
for digit in binary:
        decimal = decimal*2 + int(digit)
print("The decimal value is:", decimal)
elif decimal = input("Enter a decimal number :")
# Calling the function
DecimalToBinary(int(decimal))

def DecimalToBinary(decimal):
    if decimal > 1:
        DecimalToBinary(decimal // 2)
    print(decimal % 2, end = '')
elif 