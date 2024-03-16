public class CompareNumbers {

    public static void main(String[] args) {
      compareNumbers();
    }
  
    public static void compareNumbers() {
      Scanner scanner = new Scanner(System.in);
  
      System.out.print("Enter the first number: ");
      double firstNumber = scanner.nextDouble();
  
      System.out.print("Enter the second number: ");
      double secondNumber = scanner.nextDouble();
  
      if (firstNumber < secondNumber) {
        System.out.println(firstNumber + " is less than " + secondNumber + ".");
      } else if (firstNumber > secondNumber) {
        System.out.println(firstNumber + " is greater than " + secondNumber + ".");
      } else {
        System.out.println(firstNumber + " is equal to " + secondNumber + ".");
      }
    }
  }