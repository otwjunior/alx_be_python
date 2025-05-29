#lets draw a square
length = int(input('Enter the size of the pattern: '))
x=0
while x<length:
    for i in range(length):
        print('*', end='')
    print()
    x+=1
