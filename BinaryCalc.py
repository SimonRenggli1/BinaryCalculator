# Define Variables
number = 0

# Get Inputs
def binaryCalc():
    number = input("Do you want to convert from[f] or to[t] Binary? ")
    if number == "f":
        ##calc from Binary to decimal
        binary = input("Enter a binary number: ")
        binaryToDecimal(int(binary))

    elif number == "t":
        ##calc to Binary from decimal
        decimal = input("Enter a decimal number: ")
        decimalToBinary(int(decimal))

    else:
        print("Invalid input")
        binaryCalc()

# Function to convert binary number to decimal
def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)   

# Function to convert decimal number to binary
def decimalToBinary(decimal):
 
    if(decimal > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(decimal//2)
 
     
    print(decimal%2, end='')

# Start the program
if __name__ == '__main__':
    binaryCalc()