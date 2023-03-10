import java.util.*;
/**
 * The Class Library.
 *
 * @author Tien Tran
 */
public class Library {

    /**
     * The my books.
     *
     * @field ArrayList of Book objects
     */
    private ArrayList <Book> myBooks = new ArrayList <Book> ();;

    /*
     * Constructor - creates library with array-list of books populating theBooks
     * with book objects
     */
    // creating the constructor parameter as theOther (Book) type
    /**
     * Instantiates a new library.
     *
     * @param theOther the the other
     */
    public Library(final ArrayList <Book> theOther) {
        // TODO Auto-generated constructor stub
        // checking whether book is not empty
        if (theOther == null) {
            throw new NullPointerException("null pointer");
        } else {
            this.myBooks = theOther;
            // populating the theBooks array-list
            myBooks.addAll(theOther);

        }
    }

    /*
     * Constructor - creates library (and empty arraylist of book objects)
     */
    /**
     * Instantiates a new library.
     */
    // creating the Empty arrayList of object Book
    public Library() {
        this.myBooks = new ArrayList < Book > ();
    }

    /*
     * Adds a new book to the library after checking
     */
    /**
     * Adds the.
     *
     * @param theBook the the book
     * @return true, if successful
     */
    // checks whether the strings of book is null or empty
    public boolean add(final Book theBook) {
        // checkers whether the string is empty or null
        if (theBook == null && !theBook.equals("")) {
            throw new NullPointerException();
        } else {
            // this add method return true if book is added otherwise false
            return myBooks.add(theBook);
        }
    }

    /*
     * Get all books with specified title.
     */
    /**
     * Find titles.
     *
     * @param theTitle the the title
     * @return the array list
     */
    // retrieving the title
    public ArrayList <Book> findTitles(final String theTitle) {
        // Title array list of book object
        ArrayList <Book> Title = new ArrayList <Book> ();

        // filling the title array-list with those who matches with theTitle
        for (Book bk_ttle: myBooks) {
            // calling compareTo method
            if (bk_ttle.getTitle().compareTo(theTitle) == 0) {
                Title.add(bk_ttle);
            }
        }
        return Title;
    }

    /*
     * Sorts books by title.
     */
    /**
     * Sort.
     */
    // sorting program by professor
    public void sort() {
        Collections.sort(myBooks);
    }

    /*
     * Create a string representation of library.
     */
    /**
     * To string.
     *
     * @return the string
     */
    // output displayer
    public String toString() {
        // Add each book to dsplyr (displayer for library)
        String dsplyr = "";
        for (Book bk_displayer: myBooks) {
            dsplyr = dsplyr + bk_displayer.toString() + "\r\n";
        }

        return dsplyr;
    }
}