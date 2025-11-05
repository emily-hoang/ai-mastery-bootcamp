def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

while True:
  print("\nMenu:")
  print("1. Addition")
  print("2. Substraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == "5":
    print("Exiting")
    break
  
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  
  if choice == "1":
    print("Addition of first and second number is: ", add(num1, num2))
  elif choice == "2":
    print("Substraction of first and second number is: ", substract(num1, num2))
  elif choice == "3":
    print("Multiplication of first and second number is: ", multiply(num1, num2))
  elif choice == "4":
    print("Division of first and second number is: ", divide(num1, num2))
  else:
    print("Invalid choice.")