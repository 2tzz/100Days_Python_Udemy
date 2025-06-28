class User :
    def __init__(self , name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args , **kwargs):
        if args[0].is_logged_in == True:
          function(args[0]) 
        return wrapper

@is_authenticated_decorator
def create_blog_post(user):
     print(f"this is {user.name}'s new blog post ")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


# exercise

# TODO: Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        # return result
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)