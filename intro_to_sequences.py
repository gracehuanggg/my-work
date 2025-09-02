"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["pizza", "sushi", "pasta", "salad", "sandwich"]

# Access items by index (first = 0):
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean? 
#It can't run because there is no index 100 in the list


# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append("ice cream")
print(foods)

# TODO: Insert a food at the beginning with .insert()
foods.insert(0, "tacos")
print(foods)

# TODO: Remove one food from the list with .remove()
foods.remove("salad")
print(foods)

# TODO: How many foods are in the list? Use len()
print(len(foods))

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?
#Error, becuase chocolate is not in the list


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.


# Bug Exploration:
# Change your loop to go past the length of the list:


# Q: Why does this cause an error?
# This causes an error becuase the index goes out of the range, and the item does not exist.

# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Grace",
    "age": 16,
    "student": True,
    "favorite color": "blue"
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.


# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")
print(f"My name is {me.get('name')}")
print(f"My age is {me.get('age')}")
print(f"My favorite color is {me.get('favorite color')}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?
# It doesn't work because there is no key called hometown. The get button is useful because it prevents it from running an error.


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.
me["hobby"] = "running"


# TODO: Change the value of an existing key.
me["age"] =17

# TODO: Remove one key-value pair.
me.pop("student")
print(me)

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?
# Same as a list, it gives an error because the key doesn't exist. You can use the "none" function to prevent it from running into an error.
me.pop("grade", None)

# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()
for key in me:
    print(key)
for value in me.values():
    print(value)
for key, value, in me.items():
    print(f"{key}: {value}")

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)
# It will only print the keys without the values. 
for key in me:
    print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?
# It only prints the keys beacause that is the default behavior of looping through a dictionary. You can use the .items function to print both keys and values.

# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
friends = [
    {"name":"Kimberly", "favorite food":"matcha"},
    {"name":"Mia", "favorite food":"grapes"},
    {"name":"Loli", "favorite food":"pizza"}
]


# TODO: Print the favorite food of the second friend.
print(friends[1]["favorite food"])

# TODO: Loop through and print "<name> likes <food>" for each friend.
print(f"{friends[0]['name']} likes {friends[0]['favorite food']}")
print(f"{friends[1]['name']} likes {friends[1]['favorite food']}")
print(f"{friends[-1]['name']} likes {friends[-1]['favorite food']}")
# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?
# It gives an error because they key doesn't exist. You can use the "none" function to avoid the system from running into an error. 
print(f"friends[0].get('hobby', None)")
      
# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# A list is an ordered collection of items acessed via an index, while a dictionary are key-value pairs that can be looked up when needed.
# 2. When would you want to use a dictionary instead of a list?
# You would want to use a dictionary when you want to assoicate specific keys with specific values and pair them together.
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# A real-world situtaion where combining lists and dictionaries would be useful is in a class roster. The list allows you to call out each student, while the dictionary can document the distinct associations with each student.
# 4. What types of mistakes gave you the most errors today?
# The most errors occured when we tried to acess indexes or keys that did not exist. 
# 5. How might noticing errors actually help you learn?
# Noticing errors, especially small syntax issues, can help you learn because you can take note of what you did wrong and try to avoid that next time. 