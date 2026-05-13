# Original recipe for 4 people
recipe = {
    "pasta": 500,
    "tomatoes": 4,
    "basil": 10,
    "garlic": 2,
    "olive oil": 50
}

# Pantry stock available at home 

pantry = {
    "pasta": 300,
    "tomatoes": 10,
    "basil":4,
    "garlic":1,
    "olive oil": 100
}

original_servings = 4
party_size = 10
#scaling factor 
scale_factor = party_size / original_servings

shopping_list = []
print("Scaled Recipe:\n")

for ingredient, amount in recipe.items():
    needed_amount = amount * scale_factor

print(f"{ingredient}: {needed_amount}")

shopping_list = []
for ingredient, amount in recipe.items():
    needed_amount = amount * scale_factor

    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

#count items
items_to_buy = 0

for item in shopping_list:
    items_to_buy += 1

print("\nShopping List:")
print(shopping_list)

print("\nTotal items to buy:", items_to_buy)
                                   