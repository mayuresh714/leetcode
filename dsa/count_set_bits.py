# count set bits in a number or integer

def countSetBits(number):
    counter =  0
    while number:
        number = number & (number - 1)
        counter += 1
    return counter

if __name__ == "__main__":
    print(countSetBits(number = 15))