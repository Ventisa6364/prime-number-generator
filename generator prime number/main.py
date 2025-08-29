def all_prime_to_n(n):
    if n < 2:
        return []

    prime_list = []

    for num in range(2, n + 1):
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(num)

    return prime_list

def x_first_prime_number(x):
    list_prime_num = []
    is_prime = True
    num = 2
    
    while True:
        d = 2
        while d ** 2 <= num:
            if num % d == 0:
                is_prime = False
            
            d += 1

        if is_prime:
            list_prime_num.append(num)

        num += 1

        if len(list_prime_num) == x:
            return list_prime_num


print(all_prime_to_n(10))
print(x_first_prime_number(12))
