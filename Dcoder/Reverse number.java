import java.util.*;


import java.util.Scanner;
 
class Dcoder
 
{ 
    
	public static void main(String args[])
     
	{ 

        	
		System.out.println("Hello, Dcoder!");
        
		Scanner sc=new Scanner(System.in);
        
		int a=sc.nextInt();
        
		int rev=0;
        
		while(a!=0)
		{
        	
			int rem=a%10;
        		
			rev=rev*10+rem;
        	
			a=a/10;
      
		}
      
		System.out.println(rev);
       
		}
     
}
  
