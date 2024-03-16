class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def create_linked_list(value, recursion_type):
  # Base case (end of recursion)
  if value > 4:
    return None

  # Create a new node with the data
  new_node = Node(value)

  # Implement recursive call based on recursion type
  if recursion_type == "linear":
    new_node.next = create_linked_list(value + 1, recursion_type)
  elif recursion_type == "tail":
    return create_linked_list(value + 1, recursion_type)  # Tail recursion in Python usually involves returning the function call
  elif recursion_type == "binary":
    left_node = create_linked_list(value + 1, recursion_type)
    right_node = create_linked_list(value + 2, recursion_type)
    new_node.next = left_node
    return right_node  # Binary recursion often returns the right subtree in Python
  elif recursion_type == "mutual":
    # Implement mutual recursion logic here (requires two functions working together)
    pass
  else:
    print("Invalid recursion type!")
    return None

  return new_node

def print_list(head):
  current = head
  while current:
    print(current.data, end=" -> ")
    current = current.next
  print("None")

# Example usage (replace with your desired recursion type)
recursion_type = "linear"  # Change to "tail", "binary", or implement "mutual"
head = create_linked_list(1, recursion_type)
print_list(head)