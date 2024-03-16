import java.util.LinkedList;

public class MusicPlayer {

  public static void main(String[] args) {
    // Create linked lists
    LinkedList<String> songs = new LinkedList<>();
    LinkedList<String> artists = new LinkedList<>();
    LinkedList<String> playlist = new LinkedList<>();

    // Add song titles
    songs.add("We Belong Together");
    songs.add("Million Reasons");
    songs.add("The Climb");
    songs.add("Who You Are");
    songs.add("A Woman's Worth");

    // Add artists
    artists.add("Mariah Carey");
    artists.add("Lady Gaga");
    artists.add("Miley Cyrus");
    artists.add("Jessie J");
    artists.add("Alicia Keys");

    // Combine songs and artists into playlist
    for (int i = 0; i < songs.size(); i++) {
      playlist.add(songs.get(i) + " - " + artists.get(i));
    }

    // Display song list
    System.out.println("Songs:");
    for (String song : songs) {
      System.out.println(song);
    }

    System.out.println("\nArtists:");
    for (String artist : artists) {
      System.out.println(artist);
    }

    System.out.println("\nPlaylist:");
    for (String item : playlist) {
      System.out.println(item);
    }
  }
}