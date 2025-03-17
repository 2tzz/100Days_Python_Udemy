import os

path = r"..\..\..\my_file.txt"

with open(path , mode = "r") as file :
    reads = file.read()

    print (reads)


