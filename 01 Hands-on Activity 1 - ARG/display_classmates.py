def display_classmates():
  """Gets names of three classmates from the user and displays them."""
  # Get the first classmate's name
  first_name = input("Enter the name of your first classmate: ")

  # Get the second classmate's name
  second_name = input("Enter the name of your second classmate: ")

  # Get the third classmate's name
  third_name = input("Enter the name of your third classmate: ")

  # Display the names
  print(f"Your classmates are: {first_name}, {second_name}, and {third_name}.")

# Call the function to display names
display_classmates()