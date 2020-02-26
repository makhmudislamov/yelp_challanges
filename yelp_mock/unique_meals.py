class Meal:
    def __init__(self, name, ingredients):

        self.name = name
        self.ingredients = ingredients




def unique_meal(meals):

    unique_counter = 1

    first_m = 0
    next_m = first_m + 1
    while next_m < len(meals):
        current_meal = meals[first_m]
        # while first_m < len(meals) - 1:
        next_meal = meals[next_m]

        if sorted(current_meal.ingredients) == sorted(next_meal.ingredients):
            unique_counter -= 1
        else:
            unique_counter += 1
        next_m += 1
    return unique_counter
            

            
            



meals = [
    Meal("Basic Burger", ["Lettuce", "Tomato", "Onion", "Patty"]),
    Meal("Cheese Burger", ["Cheese", "Tomato", "Patty", "Lettuce"]),
    Meal("Jay's Burger", ["Onion", "Tomato", "Patty", "Lettuce"]),
    Meal("Sandwich", ["Tomato", "Patty", "Lettuce", "Cheese"])
]
        
print(unique_meal(meals))
