def perform_operation(num1, num2, operation):
    try:
        if operation=='add':
            return num1+num2
        elif operation=='substract':
            return num1-num2
        elif operation=='multiply':
            return num1*num2
        elif operation=='divide':
            return num1/num2
        else:
            return 'operation not allowed.'
    except ZeroDivisionError:
        return 'cannot divide by zero'
