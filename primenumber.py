
# functions starts from here:

def main():

    ask = str(input("Do you want to check you number is prime or not or want to check primes in you range given(check/range):"))

    if ask.lower() == "check":

        checker()

    elif ask.lower() == "range":

        rangechecker()

    else:
        print("Invalid input")

def loops():

    ask2 = str(input("Do you want to check again?(yes/no):"))

    while ask2.lower() == "yes":

        main()

        ask2 = str(input("Do you want to check again?(yes/no):"))

def checker():

    x = int(input("Enter the number you want to check:"))

    m = x - 1
    counter = 0

    for a in range(2,m):
        if x % a == 0:
            counter = counter + 1

    if counter == 0:
        print("its an prime")
    else:
        print("its not an prime")

def rangechecker():

    end = int(input("Enter number in which it will check:"))

    x = 2

    z = 0
    primes = []

    while z != end:
        m = x - 1
        counter = 0

        for a in range(2,m):
            if x % a == 0:
                counter = counter + 1
            else:
                continue

        if counter == 0:
            primes.append(m+1)

        x = x + 1
        z = z + 1

        for index,nums in enumerate(primes):
            if nums > end:
                primes.pop(index)
                break

    print("the prime number are:")
    print(primes)

# main code starts here:

main()

loops()