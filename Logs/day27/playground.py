#unlimited positional arguments

# def add(*args):
#     x = 0
#     for n in args :
#         x = x + n

#     return x



# addition = add(1 , 3 , 2 , 9)

# print(addition)


#many keyworded arguments

def calculate(n , **kwargs) :

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2 , add=3 , multiply=5)
