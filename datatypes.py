# Variable declaration and assignment
age = 25
name = "Alice"
# Updating variable values
age = 26
print(name)
print(age)

#membership

#declare list
fruits = ["apple", "banana", "cherry"]
#Declare string
is_apple_in_list = "apple" in fruits
is_mango_not_in_list = "mango" not in fruits
print(is_apple_in_list)
print(is_mango_not_in_list)

#identity

x = [1, 2, 3]
y = x
is_same_object = x is y
print(is_same_object)