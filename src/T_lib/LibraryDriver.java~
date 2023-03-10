
import java.util.*;
import java.io.*;
/**
 * The Class LibraryDriver.
 *
 * @author Trien Tran
 */
public class LibraryDriver {

    /** The Constant fin1. */
    private static final String fin1 = "LibraryIn1.txt";
    
    /** The Constant fin2. */
    private static final String fin2 = "LibraryIn2.txt";
    
    /** The Constant fout. */
    private static final String fout = "LibraryOut.txt";

    /**
     * The main method.
     *
     * @param args the arguments
     */
    public static void main(String[] args) {
        Library library = null;
        Scanner fileReader = null;
        ArrayList <Book> books = new ArrayList < > ();


        // read all books from input file 1
        try {
            fileReader = new Scanner(new File(fin1));
            while (fileReader.hasNextLine()) {
                // read title
                String title = fileReader.nextLine().trim();
                //read author(s)
                String[] author = fileReader.nextLine().trim().split("\\*");
                ArrayList <String> authors = new ArrayList < > ();
                for (String auth: author) {
                    authors.add(auth);
                }
                //Insert title & author(s)into a book  
                Book bk = new Book(title, authors);
                //Add this book to the ArrayList<Book> of books
                books.add(bk);
            }
            //Close the first input file and open the second input file.
            fileReader.close();
            library = new Library(books);
        } catch (FileNotFoundException e) {
            System.out.println("Could not locate file:!" + e + fin1);
            System.exit(0);
        }

        System.out.println("*** PRINTS INITIAL BOOK LIST: ***\n----------------------------------\n" + library.toString());

        // sort the books read from file 1 of the library
        library.sort();
        System.out.println("*** PRINTS SORTED BOOK LIST: ***\n---------------------------------------\n" + library.toString());


        // read all books from input file 2
        try {
            fileReader = new Scanner(new File(fin2));
            while (fileReader.hasNextLine()) {
                // read title
                String title = fileReader.nextLine().trim();
                //read author(s)
                String[] author = fileReader.nextLine().trim().split("\\*");
                ArrayList <String> authors = new ArrayList < > ();
                for (String athr: author) {
                    authors.add(athr);
                }
                //Insert title & author(s)into a book
                // Add this book to the ArrayList<Book> of books
                Book book = new Book(title, authors);
                library.add(book);
            }
            //Close all input file
            fileReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Could not locate file: " + e + fin2);
            System.exit(0);
        }

        System.out.println("*** PRINTS WITH NEW BOOKS UNSORTED: ***\n----------------------------------\n" + library.toString());

        // sort all the books from file 2 of the library
        library.sort();
        System.out.println("*** PRINTS ALL SORTED BOOK LIST: ***\n----------------------------------------\n" + library.toString());

        // write the sorted list to the file
        // writing the books of the library to the output file
        FileWriter outFile;
        PrintWriter outputFile;
        try {
            outFile = new FileWriter(new File(fout), true);
            outputFile = new PrintWriter(outFile);
            outputFile.write("*** BOOKS AFTER SORTING ***" + System.lineSeparator() + "---------------------------" + System.lineSeparator());
            outputFile.write(library.toString());
            
            // The following tests the findTitles method:
            // Write only the "Acer Dumpling" books to the output file
            outputFile.println("Acer Dumpling Books\r\n");
            outputFile.println(library.findTitles("Acer Dumpling"));
            // Write only the "The Bluffs" books to the output file
            outputFile.println("The Bluff Books\r\n");
            outputFile.println(library.findTitles("The Bluff"));
            
            outputFile.flush();
            outFile.close();
            outputFile.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        
        //The last display
        System.out.println("\r\nAcer Dumpling Books\r\n");
        System.out.println(library.findTitles("Acer Dumpling"));
        System.out.println("\r\nThe Bluff Books\r\n");
        System.out.println(library.findTitles("The Bluff"));
    }
}