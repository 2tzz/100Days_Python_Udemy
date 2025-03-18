import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

print(grey_squirrels_count)

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(red_squirrels_count)

Black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(Black_squirrels_count)



data_dic ={
    "fur_color" : ["grey" , "Cinnamon" , "Black"] , "count" : ["2473" , "392" , "103"]
}


ds =  pandas.DataFrame(data_dic)
ds.to_csv("Squirrel_count.csv")