# The Collatz Sequence

def collatz(number):                 # collatz function
    print(number," ", end= "")
    if number == 1:
        return number
    elif number%2 == 0:
        return collatz(number // 2)
    else:
        return collatz(3 * number + 1)

# main program
print("Enter a Number : ", end="")
num = int(input())
print("\nReturning : ",collatz(num))