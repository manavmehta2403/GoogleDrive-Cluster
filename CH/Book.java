import java.util.ArrayList;

/**
 * @author Tien Tran
 *
 */
public class Book implements Comparable <Book> {
	/**
	 * 
	 */
	//declaring variables
	private final String theTitle;
	private final ArrayList<String> theAuthors;
	
	/*
	 * Constructor Book : builds a book object
	*/
	//Constructor with two parameters 
	public Book(final String theTitle, final ArrayList<String> theAuthors) 
	{
		// TODO Auto-generated constructor stub
		if((theTitle == null) || (theTitle == "") || (theAuthors == null)|| (theAuthors.size() == 0) || theAuthors.isEmpty() || theTitle.isEmpty()) 
		{
		    throw new IllegalArgumentException("null or empty");
		}
		//setting the values of the variables
		this.theTitle = theTitle;
		this.theAuthors = theAuthors;
		//looping for authors name
		for (int i = 0; i < theAuthors.size(); i++)
		{
			this.theAuthors.add(i,theAuthors.get(i));
		}
	}
	
	/*
	 * This method returns the title field - gettter
	*/
	//get method is used to retrieve the title
	public String getTitle()
	{
		return this.theTitle;
	}
	
	/*
	 * his method returns the Authors field - getter
	*/
	//get method is used to create copy of authors and retrieve those authors
	//creating the defensive copy 
	public ArrayList<String> getAuthors()
	{
		return (ArrayList<String>) this.theAuthors.clone();
	}
	
	/*
	 * This method returns the formatted string - overrides toString
	*/
	//return the title and the authors of that title single book only
	public String toString()
	{
		//storing the title and the book name in one variable called displayer
		String displayer = "\"" + theTitle + ",\" by ";
		for (int i = 0; i < theAuthors.size(); i++)
		{
			displayer = displayer +theAuthors.get(i);
			//case when i is not in the AuthorsList
			if(i != theAuthors.size()-1)
			{
				displayer = displayer + ";";
			}
		}
		displayer = displayer + "\r\n";
		
		//returning displayer
		return displayer;
	}
	
	/*
	 * compares two books
	*/
	@Override
	public int compareTo(final Book theOther) {
		// TODO Auto-generated method stub
		//checks if the title matches with the other title
		if(theTitle.equals(theOther.theTitle)) {
			//if yes only checks the first author name
	     	return ((theAuthors.get(0)).compareTo(theOther.theAuthors.get(0)));
	  	}
		//moves forward to check with others 
		else {    
	     	return theTitle.compareTo(theOther.theTitle);
	  	}
	}
	
	/*
	 * compares two books to find whether they are equal or not
	*/
	public boolean equals(final Object theOther)
	{
		//checks whether theOther is Book type or not
		if(!(theOther instanceof Book))
		{
			return false;
		}
		
		//casting the theOther as Book
		Book bk_othr =(Book) theOther;
		//returns the value whether the title and book are equal or not
		return bk_othr.theTitle.contentEquals(theTitle) && bk_othr.theAuthors.equals(theAuthors);
	}
}