def find_birth_month_matches(your_month):
  """
  This function prompts the user for the birth months of six classmates,
  groups them into two sets, finds the intersection (common months),
  union (all unique months), and difference (months in one group but not the other),
  and informs the user if they share a birth month with any classmates.
  """
  group1 = set()
  group2 = set()

  # Get birth months from classmates (group 1)
  for i in range(3):
    month = input(f"Enter birth month for classmate {i+1}: ").capitalize()
    group1.add(month)

  # Get birth months from classmates (group 2)
  for i in range(3):
    month = input(f"Enter birth month for classmate {i+4}: ").capitalize()
    group2.add(month)

  # Display group information
  print("\nGroup 1:", group1)
  print("Group 2:", group2)

  # Find unions, intersections, differences
  union = group1.union(group2)
  intersection = group1.intersection(group2)
  difference = group1.symmetric_difference(group2)

  # Display sets
  print("\nUnion:", union)
  print("Intersection:", intersection)
  print("Difference:", difference)

  # Check for matching birth month
  if your_month in union:
    print("\nYou have the same birth month with at least one classmate.")
  else:
    print("\nYou don't share a birth month with any classmates in this group.")

# Get your birth month
your_month = input("\nEnter your birth month: ").capitalize()

# Call function to find matches
find_birth_month_matches(your_month)