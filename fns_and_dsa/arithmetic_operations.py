def perform_operation(num1, num2, operation):
    try:
        if operation=='add':
            return num1+num2
        elif operation=='subtract':
            return num1-num2
        elif operation=='multiply':
            return num1*num2
        elif operation=='divide':
            return num1/num2
        else:
            return 'operation not allowed.'
    except ZeroDivisionError:
        print ('cannot divide by zero')
        return 0
