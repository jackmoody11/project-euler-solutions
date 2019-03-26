def find_max_digits():
    place = 0
    count = 0
    while count <= 1000000:
        place += 1
        count += 9 * place * 10**(place-1)
    print(place)

def compute():
    my_str = ""
    prod = 1
    for i in range(999999):
        my_str += str(i)
    for i in range(7):
        prod *= int(my_str[10**i])
    print(prod)

compute()
    