import java.util.*;
/**
 * The Class Book.
 *
 * @author Tien Tran
 */

public class Book implements Comparable <Book> {

    /** The title. */
    // declaring variables
    private final String theTitle;
    
    /** The authors. */
    private final ArrayList <String> theAuthors;

    /*
     * Constructor Book : builds a book object
     */
    /**
     * Instantiates a new book.
     *
     * @param theTitle the the title
     * @param theAuthors the the authors
     */
    // Constructor with two parameters
    public Book(final String theTitle, final ArrayList <String> theAuthors) {
        // TODO Auto-generated constructor stub
        if ((theTitle == null) || (theTitle == "") || (theAuthors == null) || (theAuthors.size() == 0) ||
            theAuthors.isEmpty() || theTitle.isEmpty()) {
            throw new IllegalArgumentException("Either the title or the authors aren't there");
        }
        // setting the values of the variables
        this.theTitle = theTitle;
        this.theAuthors = theAuthors;
        this.theAuthors.addAll(theAuthors);

    }

    /*
     * This method returns the title field - getter
     */
    /**
     * Gets the title.
     *
     * @return the title
     */
    // get method is used to retrieve the title
    public String getTitle() {
        return this.theTitle;
    }

    /*
     * his method returns the Authors field - getter
     */
    // get method is used to create copy of authors and retrieve those authors
    /**
     * Gets the authors.
     *
     * @return the authors
     */
    // creating the defensive copy
    public ArrayList <String> getAuthors() {
        return (ArrayList <String>) this.theAuthors.clone();
    }

    /*
     * This method returns the formatted string - overrides toString
     */
    /**
     * To string.
     *
     * @return the string
     */
    // return the title and the authors of that title single book only
    public String toString() {
        // storing the title and the book name in one variable called displayer
        String displayer = "\"" + theTitle + ",\" by ";
        for (int i = 0; i < theAuthors.size(); i++) {
            displayer = displayer + theAuthors.get(i);
            // case when i is not in the AuthorsList
            if (i != theAuthors.size()) {
                displayer = displayer + ";";
            }
        }
        displayer = displayer + "\r\n";

        // returning displayer
        return displayer;
    }

    /**
     * Compare to.
     *
     * @param theOther the the other
     * @return the int
     */
    /*
     * compares two books
     */
    @Override
    public int compareTo(final Book theOther) {
        // TODO Auto-generated method stub
        // checks if the title matches with the other title
        if (theTitle.equals(theOther.theTitle)) {
            // if yes only checks the first author name
            return ((theAuthors.get(0)).compareTo(theOther.theAuthors.get(0)));
        }
        // moves forward to check with others
        else {
            return theTitle.compareTo(theOther.theTitle);
        }
    }

    /**
     * Equals.
     *
     * @param theOther the the other
     * @return true, if successful
     */
    /*
     * compares two books to find whether they are equal or not
     */
    public boolean equals(final Object theOther) {
        // checks whether theOther is Book type or not
        if (!(theOther instanceof Book)) {
            return false;
        }

        // casting the theOther as Book
        Book bk_othr = (Book) theOther;
        // returns the value whether the title and book are equal or not
        return bk_othr.theTitle.contentEquals(theTitle) && bk_othr.theAuthors.equals(theAuthors);
    }
}