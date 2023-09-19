spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    item_name = [ (item['name']) for item in spicy_foods]
    return item_name

def get_spiciest_foods(spicy_foods):
    spiciest_foods_list = [item for item in spicy_foods if item['heat_level'] > 5]
    return spiciest_foods_list

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        chilis = "🌶" * item["heat_level"]
        print (f'{item["name"]} ({item["cuisine"]}) | Heat Level: {chilis}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_food_list = [item for item in spicy_foods if item['cuisine'] == cuisine]
    return (cuisine_food_list[0])

def print_spiciest_foods(spicy_foods):
    print_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(print_list)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for item in spicy_foods:
        total_heat += item['heat_level']
    average_heat = total_heat / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods