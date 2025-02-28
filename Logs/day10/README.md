# Day 10 - Functions With Outputs
## Calculator App

![](calgame.gif)






## Exercises
### Excercise 1 - Days In Month
**Instructions:**
- First, convert the function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
- Then create a function called `days_in_month()` which will take a **year** and a **month** as inputs.
- It will use this information to work out the **number of days in the month,** then **return** that as the **output**.
- The List `month_days` contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

**Input Example:**
```
days_in_month(year=2022, month=2)
```

**Output Example:**
```
28
```

**Code**
<details><summary>Solution</summary>
<p>

```Python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_par, month_par):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_par) and month_par == 2:
        return 29
    else:
        return month_days[month_par -1]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

</p>
</details>

#
