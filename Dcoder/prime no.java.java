import java.util.*;


import java.util.Scanner;

class Dcoder
 
{ 
	
	public static void main(String args[])
 	
	{ 

		
		System.out.println("Hello, Dcoder!");
		
		Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		
		int f=0;
		
		if(a>1)
		{
			
			for(int i=2;i<a-1;i++)
			{
			
				if(a%i==0)
				{
				
					f=f+1;
			
				}
		
			}
			
		
		if(f==0)
		{
			
			System.out.println("prime");
		
		}
		
		else
		{
			
			System.out.println("not prime");
		
		}
		}
      
		else
		{
			System.out.println("chlna");	
		
}
	}
}
    