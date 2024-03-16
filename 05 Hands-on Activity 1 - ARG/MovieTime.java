import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class MovieTime {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    Queue<String> movies = new LinkedList<>();
    Queue<String> snacks = new LinkedList<>();

    System.out.println("Enter three movies:");
    for (int i = 0; i < 3; i++) {
      movies.add(scanner.nextLine());
    }

    System.out.println("Enter three snacks:");
    for (int i = 0; i < 3; i++) {
      snacks.add(scanner.nextLine());
    }

    System.out.println("Movies:");
    for (String movie : movies) {
      System.out.println(movie);
    }

    System.out.println("Snacks:");
    for (String snack : snacks) {
      System.out.println(snack);
    }

    while (true) {
      System.out.println("Press 'S' to finish a snack:");
      String choice = scanner.nextLine();
      if (choice.equalsIgnoreCase("S")) {
        String finishedSnack = snacks.poll();
        if (finishedSnack != null) {
          System.out.println("Finished " + finishedSnack);
          System.out.println("Remaining snacks:");
          for (String snack : snacks) {
            System.out.println(snack);
          }
        } else {
          System.out.println("No more snacks!");
          break;
        }
      }
    }
  }
}