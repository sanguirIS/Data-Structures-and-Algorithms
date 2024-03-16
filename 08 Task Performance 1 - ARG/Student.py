class Student:
  """
  A class to represent a student with a name and grade.
  """

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

def main():
  """
  The main function to manage the student list.
  """
  students = []

  # Add a few students initially
  students.append(Student("John", 88))
  students.append(Student("Mary", 95))
  students.append(Student("Peter", 77))

  while True:
    print("\nStudent List Menu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter student name: ")
      grade = float(input("Enter student grade: "))
      students.append(Student(name, grade))
      print(f"Student {name} has been added.")

    elif choice == '2':
      if not students:
        print("There are no students in the list.")
      else:
        for student in students:
          print(f"{student.name} - {student.grade}")

    elif choice == '3':
      name = input("Enter student name to search: ")
      found = False
      for student in students:
        if student.name == name:
          print(f"Student {name} - Grade: {student.grade}")
          found = True
          break
      if not found:
        print(f"Student {name} not found in the list.")

    elif choice == '4':
      print("Exiting program.")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()