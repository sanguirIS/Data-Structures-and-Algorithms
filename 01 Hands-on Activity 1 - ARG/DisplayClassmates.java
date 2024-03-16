public class DisplayClassmates {

    public static void main(String[] args) {
      displayClassmates();
    }
  
    public static void displayClassmates() {
      Scanner scanner = new Scanner(System.in);
  
      System.out.print("Enter the name of your first classmate: ");
      String firstName = scanner.nextLine();
  
      System.out.print("Enter the name of your second classmate: ");
      String secondName = scanner.nextLine();
  
      System.out.print("Enter the name of your third classmate: ");
      String thirdName = scanner.nextLine();
  
      System.out.println("Your classmates are: " + firstName + ", " + secondName + ", and " + thirdName + ".");
    }
  }