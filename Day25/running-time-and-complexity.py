from math import sqrt


def is_prime(numb):
    if numb in [2, 3, 5, 7]:
        return True

    if numb == 1 or numb % 2 == 0 or numb % 3 == 0:
        return False

    ranges = range(5, int(sqrt(int(numb))) + 1, 2)
    for number in ranges:
        if numb % number == 0:
            return False

    return True


n = input('')
pull = []
for i in range(int(n)):
    pull.append(int(input('')))

for item in pull:
    print('%s' % ('Prime' if is_prime(item) else 'Not prime'))
