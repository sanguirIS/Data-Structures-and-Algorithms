from collections import deque

classmates = deque()

# Prompt user for nicknames
print("Enter nicknames of 4 classmates:")
for _ in range(4):
  classmates.append(input())

# Simulate greeting using a loop
while classmates:
  nickname = classmates.popleft()
  print(f"Hi {nickname}!")

# Display message when queue is empty
print("Done saying hi!")