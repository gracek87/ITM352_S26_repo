# Design a conditional expression for the leap year conditional logic using a combination of AND and OR operators with specific parenthetical grouping (Condition A AND Condition B) OR Condition C. How must you ensure that the boolean operators correctly mirror the flow-chart to prevent unintended evaluation order? Test your program with your own birth year and the closest leap year to your birth year. If your birth year is a leap year, then use your birth year + 1 for the non-leap year. 
# Name: Grace Kulhanek
# Date: 02/12/2026


year = int(input("Enter a year: "))
is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

if is_leap:
    print(year, "is a leap year.")
else:
    print(year, "is NOT a leap year.")

test_years = [year, year + 1]
for y in test_years:
    is_leap = ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)
    print(y, "Leap Year?" , is_leap)
