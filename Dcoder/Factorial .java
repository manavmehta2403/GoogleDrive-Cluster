import java.util.*;


import java.util.Scanner;
 
class Dcoder
 
{ 
	
	public static void main(String args[])
 	
	{ 

		
		System.out.println("Hello, Dcoder!");
		
		Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		
		int fact=1;
		
		for (int i=1;i<=a;i++)
		{
			
			fact=fact*i;
			
			System.out.println(fact);
		
		}
		
		System.out.println(fact);

 		
	}
 
}