# Write your tests here!
from optimal_change import optimal_change
import random
import math

print(optimal_change(31.49, 50) == 'The optimal change for an item that costs $31.49 with an amount paid of $50.00 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 2 quarters, and 1 penny.')
print(optimal_change(.01, .01) == 'You are owed no change')
print(optimal_change(189.01, 256.89) == 'The optimal change for an item that costs $189.01 with an amount paid of $256.89 is 1 $50 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 3 pennies.')
print(optimal_change(6, 6.75) == 'The optimal change for an item that costs $6.00 with an amount paid of $6.75 is 3 quarters.')
print(optimal_change(.05, .01) == 'You are owed no change')

# count = 0.01
# while count < 100:
#     rand = random.randrange(0,math.ceil(count), 1)
#     print(optimal_change(rand, round(count, 2)))
#     count+=0.01