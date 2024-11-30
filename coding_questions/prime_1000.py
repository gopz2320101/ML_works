nums=range(1,1000)

def Is_prime(num):
    for x in range(2,num):
        if (num % x) == 0:
            return False
    return True

prime=list(filter(Is_prime,nums))
print(prime)

#prints prime numbers from 0 to 1000