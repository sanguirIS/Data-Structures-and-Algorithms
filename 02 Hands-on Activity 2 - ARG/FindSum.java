public class FindSum {

    public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
  
      System.out.print("Enter a number: ");
      int num = scanner.nextInt();
  
      int sum = findSum(num);
      System.out.println("The sum of the first " + num + " integers is " + sum + ".");
    }
  
    public static int findSum(int n) {
      if (n == 0) {
        return 0;
      } else {
        return n + findSum(n - 1);
      }
    }
  }