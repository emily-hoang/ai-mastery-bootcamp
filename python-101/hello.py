print("Hello!!!!!!!")

# Data types
integer_var = 10
float_var = 3.24
string_var = "hey"
list_var = [1, 2, 3]
tuple_var = (4, 6, 7)
dict_var = {
  "name": "Emily",
  "age": "32"
}
bool_var = True

print("Here are my vars", integer_var, float_var, string_var, tuple_var, dict_var, list_var)

# Condition - Control Flow
num = 10
if num > 0:
  print("Possitive Number!!!!!")
elif num == 0:
  print("Number is not positive nor negative")
else:
  print("Number is negative")
  
# Loop
# For loop
items = ["TV", "chair", "monitor"]
for item in items:
  if item == "chair":
    print("The item is now chair. Stopping the loop!")
    break
  if item == "monitor":
    continue
  print("In my list for loop example, the item is:", item)
  
# For loop with range
for i in range(5):
  print("The number in the range up to 5 (exclude 5) is", i)
  
# while loop
count = 5
while count > 0:
  print("The while loop is running because the count is greater than 0")
  count -= 1
  
  