# from turtle import Turtle , Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("Darkgreen")

# timmy.forward(100)



# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()


print(table)

table.add_column("Pokemon Name",["Pikachu" , "Squuirtle" , "Charmander"])
table.add_column("Type",["Electric" , "Water" , "Fire"])

print(table)

table.align = "l"

print(table)