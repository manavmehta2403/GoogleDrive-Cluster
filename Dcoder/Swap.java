import java.util.*;
import java.util.Scanner;
class Dcoder
{
	public static void main(String agr[])
	{
		Scanner sc=new Scanner (System.in);
                int a=sc.nextInt();
                int b=sc.nextInt();
		System.out.println(a);
		System.out.println(b);
		int temp=a;
		a=b;
		b=temp;
		System.out.println(a);
		System.out.println(b);
	}
}