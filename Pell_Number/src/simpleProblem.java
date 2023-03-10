import java.util.*; 
import java.lang.*; 
import java.io.*; 
	
	public class simpleProblem {
	

		public static void main (String[] args) throws java.lang.Exception
		{
	

			String filePath = "classnames.txt";
			int nameCount = 0;
			int charCount = 0;
	    
			BufferedReader lineReader = new BufferedReader(new FileReader(filePath));
			String lineText = null;
			//extra string variable to delete spaces between the names
			String linetext_without_white_spaces = null;
			//String to retrieve the longest list
			String longest_name = "";
			while ((lineText = lineReader.readLine()) != null) {
				//(\\s+) checks the spaces and replace with ""
				linetext_without_white_spaces = lineText.replaceAll("\\s+", "");
				System.out.printf("%s has %d characters\n",lineText,linetext_without_white_spaces.length());
				charCount+= linetext_without_white_spaces.length();
				nameCount++;
				
				//to find the longest word
				//check the length of line text  whether it is greater than longest name text
				if (linetext_without_white_spaces.length() >= longest_name.length()) {
					//assigning the value for the longest value to the line text
					longest_name = lineText;
				}
			} 
			lineReader.close();
			
		//printing the longest name
	    System.out.println("\n\t\tThe longest name "+longest_name+"\n");	
	    
	    System.out.printf("out of %d student names the average number of characters is %2f\n", nameCount, (double)charCount/nameCount);
	    
	  }
	}