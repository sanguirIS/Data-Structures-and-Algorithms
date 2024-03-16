import java.io.IOException;

public class CreateFolder {

  public static void main(String[] args) {
    String folderName = "lastname_firstname"; // Replace with your lastname and firstname
    String fullPath = "C:/desired/location/" + folderName; // Replace with your desired location

    try {
      // Build the command based on your operating system
      String command =  (System.getProperty("os.name").startsWith("Windows") ? "cmd /c mkdir " : "mkdir ") + fullPath;
      Runtime.getRuntime().exec(command);
      System.out.println("Folder created successfully: " + fullPath);
    } catch (IOException e) {
      System.out.println("Error creating folder: " + e.getMessage());
    }
  }
}