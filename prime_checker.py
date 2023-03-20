n = 17

def primchecker(n):
    is_prime = True
    for i in range(2, int(n/2)):

        temp = n % i



        if temp == 0:
            is_prime = False
            break

    if is_prime == True:
        print(f"{n} is prime number")
    else:
        print(f"{n} isn't a prime number")



primchecker(n)
