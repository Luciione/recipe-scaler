# Original recipe for 4 people
recipe = {
    "pasta": 500,
    "tomatoes": 4,
    "basil": 10,
    "garlic": 2,
    "olive oil": 50
}

print(recipe)

# Pantry stock available at home 
pantry = {
    "pasta": 300,
    "tomatoes": 10,
    "basil":4,
    "garlic":1,
    "olive oil": 100
}

print(pantry)

#Original serving size
original_servings = 4
#party size
party_size = 10
#scaling factor 
scale_factor = party_size / original_servings

print(scale_factor)

print("Scaled Recipe Quantities:")

for ingredient, amount in recipe.items():
    needed_amount = amount * scale_factor
    print(ingredient, ":", needed_amount)

shopping_list = []
for ingredient, amount in recipe.items():
    needed_amount = amount * scale_factor

    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping List:")
print(shopping_list)

                                   