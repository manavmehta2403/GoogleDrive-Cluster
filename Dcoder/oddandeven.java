import java.util.*;

import java.util.Scanner;
 /*Please dont change class name, Dcoder 
 and class must not be public*/

 //Compiler version JDK 1.8


 class Dcoder
 { 
	public static void main(String args[])
 	{ 

		System.out.println("Hello, Dcoder!");
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		if (a%2==0)
		{
		 System.out.println("even");
		}
		else{
			System.out.println("odd");
		}

 	}
 }