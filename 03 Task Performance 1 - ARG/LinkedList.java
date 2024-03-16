public class LinkedList {
    public static void main(String[] args) {
      // Replace "YourRecursionType" with actual recursion type (e.g. linearRecursion)
      Node head = YourRecursionType(1); 
      printList(head);
    }
  
    // Node class to represent a single element in the linked list
    public static class Node {
      int data; // This can be changed to store the actual data type (String, etc.)
      Node next;
  
      public Node(int data) {
        this.data = data;
        this.next = null;
      }
    }
  
    // Replace "YourRecursionType" with the actual recursion function based on assignment
    public static Node YourRecursionType(int value) {
      // Implement your recursive logic here to create the linked list with desired values
      // Base case (end of recursion)
      if (value > 4) {
        return null;
      }
  
      // Create a new node with the data (replace with your chosen data type)
      Node newNode = new Node(value);
  
      // Implement recursive call to build the rest of the list based on recursion type
      newNode.next = YourRecursionType(value + 1);
  
      return newNode;
    }
  
    public static void printList(Node head) {
      Node current = head;
      while (current != null) {
        System.out.print(current.data + " -> ");
        current = current.next;
      }
      System.out.println("null");
    }
  }