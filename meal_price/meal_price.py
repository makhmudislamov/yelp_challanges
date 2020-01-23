#!/usr/local/bin/python3
"""
given the customers' list, check if the customer qualifies for discount.
1st time - 10%
2nd time - 20%
3rd time - 30%
more than 3 times - always 30%
"""
import sys
import json
data = json.load(sys.stdin)

MEAL_PRICE = 10
MAXIMUM_DISCOUNT = 0.3


def get_meal_price(customer_email: str) -> float:
    #TODO: Write this
    
    pass



assert(get_meal_price("bashard5@sun.com") == 9.0)
assert(get_meal_price("nlohana@yelp.com") == 10.0)
assert(get_meal_price("jsirett2@csmonitor.com") == 7.0)
