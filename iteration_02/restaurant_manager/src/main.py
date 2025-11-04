import json

# Need path to data file
file_path = 'restaurant_data.json'

# --- Step 1: Load JSON data into a Python dictionary ---
with open(f"{file_path}restaurant_data.json", "r") as file:
    restaurant_data = json.load(file)  # json.load reads JSON into a dict

print (restaurant_data)

restaurant_name = restaurant_data.get("name", "Search item not found")
restaurant_location = restaurant_data.get("location")
restaurant_menu = restaurant_data.get("menu")

def view_menu():
    for category in restaurant_menu:
        print(f"{category[category]} of the season: \n")
        items_list = category["items"]
        for item in items_list:
            print(f"Item{item["id"]}: ["item[name]"]... Price: {item["price"]}")
            print ("\n")

def add_menu_item():

view_menu()
add_menu_item()

user_choice = input ("Enter an option ...")
if user_choice == "view menu":
    view_menu()
