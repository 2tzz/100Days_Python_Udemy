from art import logo



def calculator_fun(input_val1 , input_val2 , operator) :

    if operator == '+' :
        return input_val1 + input_val2
    
    elif operator == '-' :

        return input_val1 - input_val2
    
    elif operator == '*' :
        return input_val1 * input_val2
    
    elif operator == '/' :
        return input_val1 / input_val2
    
    else:
        print("operator error")



print(logo)

direction = 'y'
input_1 = 0
input_2 = 0
op_select = ''
output = 0

input_1 = float(input("What is your frist number : "))

while direction == 'y' or 'n' :

    

    op_select = input(" + \n - \n * \n / \n pick an operation : ")

    input_2 = float(input("Whats the next number : "))

    output = calculator_fun(input_1 , input_2, op_select)

    print (f"{input_1} {op_select} {input_2} = {output}")

    direction = input(f"Type 'y' to continue calculating with {output} , or type 'n to start a new calculation : ")

    if direction == 'y' :

        input_1 == 0
        input_1 = output
        
        print(f"frist number {input_1}")

    elif direction == 'n' :

        input_1 = float(input("What is your frist number : "))


#done