#match case calculator
num1= int(input('Enter the first number: '))
num2= int(input('Enter the second number: '))
operators = input('Choose the operation (+,-,*,/): ')

try:
    match operators:
        case '+':
            print(f'The result is {num1+num2}.')
        case '-':
            print(f'The result is {num1-num2}.')
        case '*':
            print(f'The result is {num1*num2}.')
        case '/':
            print(f'The result is {num1/num2}.')
        case _:
            print('Such operation is allowed')
        
except ZeroDivisionError:
    print('Cannot divide by zero.')