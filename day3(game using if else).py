print("welcome to roller coster !")
height = int(input("Enter your height : "))


if height >=  120 :
    print(" you can ride the rollercoster")

    age =  int(input("Enter your age : "))


    bill = 0

    if age <= 12:
        print("please pay 5 $")
        bill = 5
    elif age <= 18:
        print("please pay 7 $")
        bill = 7
    else :
        print("please pay 12 $")
        bill = 12

    pic = input("do you want a photo?")

    if pic == 'yes' and age <= 12:
            bill = bill + 3
            print(f"yor total will be  : {bill} $")
    
    else:
          print(f"please pay the total : {bill} $ ")

else :
    print("sorry you can't ride this get taller to ride this")


















