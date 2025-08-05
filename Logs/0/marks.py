marks = []
marks_list = []

while True:
    name = input('Enter your name: ')
    if name.lower() == 'end':
        break
    mark = input('Enter your marks: ')
    
    try:
        mark = float(mark)  
    except ValueError:
        print("Please enter a valid number for marks.")
        continue

    dictionary = {'name': name, 'mark': mark}
    marks.append(dictionary)
    marks_list.append(mark) 


if marks_list:
    maxmark = max(marks_list)
    minmark = min(marks_list)
    avgmark = sum(marks_list) / len(marks_list)

    print("\nAll Marks Data:", marks)
    print(f"Maximum Mark: {maxmark}")
    print(f"Minimum Mark: {minmark}")
    print(f"Average Mark: {avgmark:.2f}")
else:
    print("No marks were entered.")





# Input 5 marks and display grades
for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    
    if mark > 75:
        grade = "A"
    elif mark >= 65:
        grade = "B"
    elif mark >= 55:
        grade = "C"
    elif mark >= 45:
        grade = "S"
    else:
        grade = "F"
    
    print(f"Mark: {mark} → Grade: {grade}")



#part d
total = 0

while True:
    num = float(input("Enter a number (-999 to stop): "))
    if num == -999:
        break
    total += num

print("Sum of numbers:", total)
