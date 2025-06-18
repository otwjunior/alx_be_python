def safe_divide(numerator, denominator):
    try:
        answer=float(numerator) / float(denominator)
        return f'The result of the division is {answer}'
    except ValueError:
        return 'Error: Please enter numeric values only.'
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
