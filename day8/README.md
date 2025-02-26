# Day 8 - Function Parameters & Caesar Cipher
## Caesar Cipher

![](Ceaser_Chiper.gif)




## Exercises
### Excercise 1 - Paint Area Calculator
**Instructions:**
- You are painting a wall. 
- The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
- Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

```
number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5

                           = 1.6
```

- Because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

**Input Example:**
```
test_h = 3
test_w = 9
```

**Output Example:**
```
You'll need 6 cans of paint.
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
#Write your code below this line 👇

import math
def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```

</p>
</details>

#

### Excercise 2 - Prime Number Checker
**Instructions:**
- Prime numbers are numbers that can only be cleanly divided by themselves and 1.
- Write a function that checks whether if the number passed into it is a prime number or not.
- E.g. 2 is a prime number because it's only divisible by 1 and 2.
- But 4 is not a prime number because you can divide it by 1, 2 or 4.

**Input Example:**
```
73
```

**Output Example:**
```
It's a prime number
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.") 
    else:
        print("It's not a prime number.")       

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
```

</p>
</details>

#
