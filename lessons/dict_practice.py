"""Practicing with Dictionaries."""

#Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(ice_cream)

#Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print(ice_cream)

#Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print(ice_cream)

#Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Adjusting a value
ice_cream["vanilla"] = 10
print(ice_cream)

#Getting the length
print(f"The number of flavors I'm offering or the number of key value pairs: {len(ice_cream)}")

#Checking if value is in dictionary
print("chocolate" in ice_cream)
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else:
    print("no orders of mint")

#Loop thorugh and print out every flavor and its number of orders
for key in ice_cream:
    #print <flavor> has <num_orders> orders
    print(f"{key} has {ice_cream[key]} orders.")