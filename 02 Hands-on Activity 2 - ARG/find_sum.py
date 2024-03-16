def find_sum(n):
  """
  Calculates the sum of the first n integers using recursion.

  Args:
      n: The non-negative integer representing the number of terms to sum.

  Returns:
      The sum of the first n integers.
  """
  if n == 0:
    return 0
  else:
    return n + find_sum(n - 1)

# Get user input for the number of terms
num = int(input("Enter a number: "))

# Calculate and display the sum
sum_of_n = find_sum(num)
print(f"The sum of the first {num} integers is {sum_of_n}.")