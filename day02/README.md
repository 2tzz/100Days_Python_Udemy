# Day 3 - Control Flow and Logical Operators
## Treasure Island

![](Tresure_hunt.gif)



## Exercises 
### Exercise 1 - Odd or Even
**Instructions:**
- Write a program that works out whether if a given number is an odd or even number.
- All even numbers can be divided by 2 with no remainder.
- e.g. 86 is even because 86 ÷ 2 = 43
- 43 does not have any decimal places. Therefore the division is clean.
- e.g. 59 is odd because 59 ÷ 2 = 29.5
- 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

> NOTE: The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

No remainder
</br> `6 ÷ 2 = 3` 

Remainder
</br> `6 % 2 = 0`

**Input Example:**
```
43
```
**Output Example:**
```
This is an odd number.
```
**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
r = number % 2 
if r == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

</p>
</details>

#

### Exercise 2 - BMI 2.0
**Instructions:**
- Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
- It should tell them the interpretation of their BMI based on the BMI value.
  - Under 18.5 they are underweight.
  - Over 18.5 but below 25 they have a normal weight.
  - Over 25 but below 30 they are slightly overweight.
  - Over 30 but below 35 they are obese.
  - Above 35 they are clinically obese.

![](bmi_chart.png)
> NOTE: The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

```math
BMI = {weight(kg) \over height^2(m^2)}
```
> WARNING: **Round** the result to the nearest whole number. 
> The interpretation message needs to include the words in bold from the interpretations above. 
> e.g. **underweight, normal weight, overweight, obese, clinically obese.**

**Input Example:**

```
weight = 85
height = 1.75
```

**Output Example:**

```
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
```

**Code**
- Try to use the exponent operator in your code.
- Remember to round your result to the nearest whole number.
- Make sure you include the words in bold from the interpretations.

**Output Example:**

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2))
#f = "{:.2f}".format(bmi)
#print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
```

</p>
</details>

#

### Exercise 3 - Leap Year
**Instructions:**
- Write a program that works out whether if a given year is a leap year. 
- A normal year has 365 days, leap years have 366, with an extra day in February.
- Learn more about leap years: [What is a Leap Year](https://www.youtube.com/watch?v=xX96xng7sAE)
- How to work out whether if a particular year is a leap year:
  - On every year that is evenly divisible by 4 
  - **Except** every year that is evenly divisible by 100 
  - **Unless** the year is also evenly divisible by 400

```
e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.

The year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
```

**Input Example:**
```
2400
```
**Output Example:**
```
Leap year.
```
**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    Print("Not leap year.")
```

</p>
</details>

#

### Exercise 4 - Pizza Order Practice
**Instructions:**
- Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
- Based on a user's order, work out their final bill.

```
  - Small Pizza: $15
  - Medium Pizza: $20
  - Large Pizza: $25

  - Pepperoni for Small Pizza: +$2
  - Pepperoni for Medium or Large Pizza: +$3

  - Extra cheese for any size pizza: + $1
```

**Input Example:**

```
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
```

**Output Example:**

```
Your final bill is: $28.
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

```

</p>
</details>

#

### Exercise 5 - Love Calculator
**Instructions:**
- write a program that tests the compatibility between two people.
- To work out the love score between two people:
  - Take both people's names and check for the number of times the letters in the word TRUE occurs. 
  - Then check for the number of times the letters in the word LOVE occurs. 
  - Then combine these numbers to make a 2 digit number.
> The lower() function changes all the letters in a string to lowercase.

> The count() function will give you the number of times a letter occurs in a string.

For Love Scores **less than 10** *or* **greater than 90**, the message should be:
```
"Your score is **x**, you go together like coke and mentos."
```

For Love Scores **between 40** *and* **50**, the message should be:
```
"Your score is **y**, you are alright together."
```

Otherwise, the message will just be their score. e.g.:
```
"Your score is **z**."
```

e.g.
```
name1 = "Jim Halpert"
name2 = "Pamela Beesly"
```
T occurs 1 times

R occurs 1 time

U occurs 0 times

E occurs 4 times

Total = 6

L occurs 3 time

O occurs 0 times

V occurs 0 times

E occurs 4 times

Total = 7

Love Score = 67

Print: "Your score is 67."



**Input Example:**
```
name1 = "John Krasinski"
name2 = "Emily Blunt"
```
**Output Example:**
```
Your score is 44, you are alright together.
```
**Code**
<details><summary>Solution</summary>
<p>

```Python
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

together = name1 + " " + name2

lower_together = together.lower()

t = lower_together.count("t")
r = lower_together.count("r")
u = lower_together.count("u")
e = lower_together.count("e")

true_total = str(t + r + u + e) 

l = lower_together.count("l")
o = lower_together.count("o")
v = lower_together.count("v")
e = lower_together.count("e")

love_total = str(l + o + v + e)

score = int(true_total + love_total)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
```

</p>
</details>
