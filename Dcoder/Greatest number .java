import java.util.*;

import java.util.Scanner;
 
class Dcoder
 
{ 
	
	public static void main(String args[])
 	
	{ 

		
		System.out.println("Hello, Dcoder!");
		
		Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		
		int b=sc.nextInt();
			
		int c=sc.nextInt();
		
		if(a>b)
		{
			
			if(a>c)
			{
				
				System.out.println("the greatest no is \n" +a);
			
			}
			
			else
			{
				
				System.out.println("the greatest no is" +c);
			
			}
			
		
		}
				
		else if(b>c)
		{
			
			System.out.println("the greates no is" +b);
			
		}
		
		else
		{
			
			System.out.println("the greatest no is"+c);
		
		}
	

}
}
    