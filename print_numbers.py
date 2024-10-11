# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497
integers = int(input('Enter a positive integer: '))
count = integers

for number in range(integers, 0, -1):
    for numbers in range(1, number+1):
        print(numbers, end=' ')
    print()