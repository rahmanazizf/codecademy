def mult_by_2(num):
    """
    prints value multiplied by 2
    param: num <int>
    """
    print(num * 2)

def get_math_function(operation):
    """
    returns math function as an object
    param: operation <str>
    """
    def add(n1, n2):
        return n1+n2
    
    def substraction(n1, n2):
        return n1 - n2
    
    def multiplication(n1, n2):
        return n1 *  n2

    def division(n1, n2):
        return n1 / n2
    
    if operation == '+':
        return add
    elif operation == '-':
        return substraction
    elif operation == 'x':
        return multiplication
    elif operation == '/':
        return division
    else:
        print("Operation error")

add_func = get_math_function('+')
# print(add_func(10, 20))

def calculate():
    """
    perform arithmetic operations
    params: None
    note: this function is not sensitive to order of operation
    make sure you entered operation accordingly
    """
    i = 0

    while True:
        if i == 0:
            number1 = int(input("Insert a number: "))
        op = input("Insert the operation: ")
        if op == '=':
            print(result)
            break
        number2 = int(input("Insert another number: "))
        
        opFunction = get_math_function(op)
        if i == 0:
            result = opFunction(number1, number2)
        else:
            result = opFunction(result, number2)

        i += 1

# calculate()

def occupation(print_my_name):
    def wrapper(*args, **kwargs):
        print("Student")
        print_my_name(*args, **kwargs)
    
    return wrapper

@occupation
def print_my_name(name):
    print(name)

# by using decorator we can associate a function with another function implicitly

