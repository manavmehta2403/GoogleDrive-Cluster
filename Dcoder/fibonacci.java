import java.util.*;


import java.util.Scanner;
 
class Dcoder
 
{ 
	
	public static void main(String args[])
 	
	{ 

		
		System.out.println("Hello, Dcoder!");
		
		Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		
		int x=0;
		
		int y=1;
			
		System.out.println(x);
		
		System.out.println(y);
		
		for(int i=0;i<a;i++)
		{
				
			int f=x+y;
				
			x=y;
				
			y=f;
				
			System.out.println (f);
				
		   
		}
			
	
	}
}
    
    