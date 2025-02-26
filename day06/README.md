# Day 5 - Python Loops
## PyPassword Generator

![](pypassword_generator.gif)






## Exercises
### Excercise 1 - Average Height
**Instructions:**
- Write a program that calculates the average student height from a List of heights.
- E.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`
- The average height can be calculated by adding all the heights together and dividing by the total number of heights.

E.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146 <br>
There are a total of 7 heights in student_heights <br>
1146 ÷ 7 = 163.71428571428572 <br>
Average height rounded to the nearest whole number = 164

> IMPORTANT: Don't use the **len()** or **sum()** functions. Try replicating their functionality with for loops.


**Input Example:**
```
156 178 165 171 187
```

**Output Example:**
```
171
```
> IMPORTANT: Use **round()** function to round final answer.

**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Replicate sum() function with for loop
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)


#Replicate len() function with for loop
num_students = 0
for student in student_heights:
    num_students += 1
#print(num_students)

average_height = round(total_height / num_students)

print(average_height)
```

</p>
</details>

#

### Excercise 2 - High Score
**Instructions:**
- Write a program that calculates the highest score from a List of scores.
- E.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

> IMPORTANT: Don't use the **max()** or **min()** functions.

**Input Example:**
```
78 65 89 86 55 91 64 89
```

**Output Example:**
```
The highest score in the class is: 91
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
```

</p>
</details>

#

### Excercise 3 - Adding Even Numbers 
**Instructions:**
- Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
- I.e. `2 + 4 + 6 + 8 +10 ... + 98 + 100`
- Use **range()** function

> IMPORTANT: there should only be 1 print statement in the console output. It should just print the final total and not every step of the calculation.

**Code**
<details><summary>Solution</summary>
<p>

```Python
#Write your code below this row 👇

total = 0
for number in range(2, 101, 2):
    total += number
print(total)
```

</p>
</details>

#

### Excercise 4 - FizzBuzz
**Instructions:**
- Write a program that automatically prints the solution to the FizzBuzz game.
- The program should print each number from 1 to 100 in turn.
- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
> Answer should start from 1 and go up to and including 100. Each number/text should be printed on a separate line.

**Output Example:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
#Write your code below this row 👇

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

```
> Proud of myself for getting it the first try! 😀

</p>
</details>
