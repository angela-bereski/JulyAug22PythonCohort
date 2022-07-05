num1 = 42 # variable declaration, integer
num2 = 2.3 # variable declaration, float
boolean = True # boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # type check, log statement
print(pizza_toppings[1]) # list access value, log statement
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # dictionary access value, log statement
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # tuple access value, log statement

if num1 > 45: # conditional, if
    print("It's greater") # log statement
else: # condition, else
    print("It's lower") # log statement

if len(string) < 5: # length check, conditional if
    print("It's a short word!") # log statement
elif len(string) > 15: # length check, conditional else if
    print("It's a long word!") # log statement
else: # conditional else
    print("Just right!") # log statement

for x in range(5): # for loop, start, stop
    print(x)  # log statement
for x in range(2,5): # for loop, start, stop
    print(x) # log statement
for x in range(2,10,3): # for loop, start, stop, step
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # While loop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # list, delete last value
pizza_toppings.pop(1) # list, delete indexed value

print(person) # log statement, dictionary
person.pop('eye_color') # dictionary, delete value
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional, if
        continue # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional, if
        break # break

def print_hello_ten_times(): # function
    for num in range(10): # for loop, start, stop
        print('Hello') # log statement

print_hello_ten_times() # function

def print_hello_x_times(x): # function, parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_times(4) # function, argument

def print_hello_x_or_ten_times(x = 10): # function, parameter
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # function
print_hello_x_or_ten_times(4) # function, argument


"""
Bonus section
"""

# print(num3)  NameError: name <num3> is not defined
# num3 = 72  NameError: name <num3> is not defined
# fruit[0] = 'cranberry'  TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  KeyError: 'favorite_team"
# print(pizza_toppings[7])  IndexError: list index out of range
#   print(boolean)  IndentationError: unexpected indent
# fruit.append('raspberry')  AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  AttributeError: 'tuple' object has no attribute 'pop'