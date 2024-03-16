def compare_numbers():
  """Compares two numbers entered by the user and displays a message."""
  # Get the first number from the user
  first_number = float(input("Enter the first number: "))

  # Get the second number from the user
  second_number = float(input("Enter the second number: "))

  # Compare the numbers and display a message
  if first_number < second_number:
    print(f"{first_number} is less than {second_number}.")
  elif first_number > second_number:
    print(f"{first_number} is greater than {second_number}.")
  else:
    print(f"{first_number} is equal to {second_number}.")

# Call the function to compare numbers
compare_numbers()