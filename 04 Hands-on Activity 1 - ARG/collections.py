from collections import deque

# Define fruits dictionary for easier fruit name retrieval
fruits = {
    "A": "Apple",
    "O": "Orange",
    "M": "Mango",
    "G": "Guava"
}

# Create an empty deque to represent the fruit basket (functions like a stack)
basket = deque()

# Get the number of fruits from the user
num_fruits = int(input("How many fruits would you like to add to the basket? "))

# Loop for adding fruits
for _ in range(num_fruits):
  # Prompt user to choose a fruit
  fruit_choice = input("Enter A for Apple, O for Orange, M for Mango, or G for Guava: ").upper()

  # Check for valid input
  if fruit_choice not in fruits:
    print("Invalid choice. Please enter A, O, M, or G.")
    continue

  # Add the chosen fruit to the basket
  fruit_name = fruits[fruit_choice]
  basket.append(fruit_name)
  print(f"Added {fruit_name} to the basket.")

# Check if the basket is empty before eating fruits
if not basket:
  print("The basket is empty!")
else:
  # Prompt user to start eating fruits
  eat_fruit = input("Do you want to start eating fruit? (Enter E): ").upper()

  while eat_fruit == "E":
    # Remove and display the eaten fruit
    eaten_fruit = basket.pop()
    print(f"You ate {eaten_fruit}.")

    # Display remaining fruits
    if basket:
      print(f"Fruits remaining in the basket: {', '.join(basket)}")
    else:
      print("The basket is now empty!")

    # Ask again if the user wants to eat more fruit
    eat_fruit = input("Do you want to eat another fruit? (Enter E or anything else to quit): ").upper()

print("Thank you for using the fruit basket program!")