# new_data = []

# with open(r"weather_data.csv") as data_file:

#     data = data_file.readlines()

# print(data)

# for line in data :
#   new_line =   line.strip()
#   new_data.append(new_line)

# print(new_data)

# import csv

# with open(r"weather_data.csv") as data_file:

#     data = csv.reader(data_file)
#     temperatures = []
#     temp = []

#     for row in data :
#         x = row[1]
#         temperatures.append(x)


# del temperatures[0]

# print(temperatures)
        
import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.temp)

print(data[data.temp == data.temp.max()])