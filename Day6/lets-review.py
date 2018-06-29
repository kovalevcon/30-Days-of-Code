
def print_result(string):
    even = string[0]
    odd = ''
    for key in range(1, len(string)):
        if key % 2 == 0:
            even += string[key]
        else:
            odd += string[key]

    print("{} {}".format(even, odd))


count = int(input())

strings = []
for row in range(count):
    strings.append(str(input()))

for row in strings:
    print_result(row)
