returned_date = [int(x) for x in input('').split(' ')]
due_date = [int(x) for x in input('').split(' ')]

hackos = 0
if due_date[2] < returned_date[2]:
    hackos = 10000
elif due_date[2] == returned_date[2]:
    if due_date[1] < returned_date[1]:
        hackos = 500 * (returned_date[1] - due_date[1])
    elif due_date[0] < returned_date[0]:
        hackos = 15 * (returned_date[0] - due_date[0])

print(hackos)

