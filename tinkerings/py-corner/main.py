print("start")
"""
Given a positive integer, calculate the sum of all the squares of the digits of the number. Input: A single line that contains a positive integer (n). Output: Print the sum of squares of the digits of the number on a single line.
"""
def sum_of_square_digits(n):
    i, result = 0, 0
    while i < len(str(n)):
        result += int(str(n)[i])**2
        i += 1
    return result

n = 111 #int(input("input your number here: "))
print(sum_of_square_digits(n))


"""
Write a program that will help people who are going on vacation. The program should calculate the total required sum (e.g. $) of money to have a good rest for a given duration.

There are four parameters that have to be considered:
- duration in days
- total food cost per day
- one-way flight cost
- cost of one night in a hotel (the number of nights is equal to the duration of days minus one)

Read integer values of these parameters from the standard input and then print the result.
"""
duration_in_days = 3 #int(input())
total_food_cost_per_day = 20 #int(input()) * duration_in_days
one_way_flight_cost = 200 #int(input()) * 2
cost_of_one_night_in_hotel = 100#int(input()) * (duration_in_days - 1)

print(total_food_cost_per_day + one_way_flight_cost + cost_of_one_night_in_hotel)


"""
Write a program that takes two integers as input, representing the length and width of a rectangle, and prints the perimeter and area of the rectangle.
"""
print("Perimeter and area of a rectangle")
length, width = 5, 3 #int(input()), int(input())
perimeter = (2 * length) + (2 * width)
area = length * width 

print(perimeter)
print(area)

"""
min() and max() is that these functions can help you to sort in alphabetical order! If a string is passed as an argument, min() will return the first letter (alphabetically) and max() the last one (somewhat zetabetically).
"""

print(max("gloomy", "grew", "green"))
print(min("gloomy", "grey", "green"))
print(min("green", "grass"))
print(max("gloomy", "grey", "green"))

"""
Boolean
"""
print(5 and 0 and 12)
print(True or False)
print(not (False or True))
print(5 or " ")

print("---")
is_raining = True
have_umbrella = True
should_stay_home = is_raining and not have_umbrella
message = "Should I stay home? " + str(should_stay_home)
print(message)