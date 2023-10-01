numbers = list(range(1, 101))

for x in numbers:
    is_prime = True

    for deler in numbers:
        if x > deler > 1:
            if x % deler == 0:
                is_prime = False
                break
    
    if is_prime:
        print(x)