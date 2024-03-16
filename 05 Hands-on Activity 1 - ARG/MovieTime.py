from collections import deque

movies = deque()
snacks = deque()

for _ in range(3):
  movies.append(input("Enter a movie: "))

for _ in range(3):
  snacks.append(input("Enter a snack: "))

print("Movies:")
for movie in movies:
  print(movie)

print("Snacks:")
for snack in snacks:
  print(snack)

while True:
  choice = input("Press 'S' to finish a snack: ").upper()
  if choice == "S":
    finished_snack = snacks.popleft()
    if finished_snack:
      print(f"Finished {finished_snack}")
      print("Remaining snacks:")
      for snack in snacks:
        print(snack)
    else:
      print("No more snacks!")
      break