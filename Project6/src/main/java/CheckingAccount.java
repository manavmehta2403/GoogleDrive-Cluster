import java.util.Random;



public class CheckingAccount extends BankAccount{

	CheckingAccount(String s, String n, String a, float f)

	{

		this.first_name = s;

		this.last_name = n;

		this.social_security_number = a;

		this.balance = f;

		Random rand = new Random();

		int num = rand.nextInt(900000000) + 1000000000;

		if((a.charAt(0) >= 48 && a.charAt(0) <= 57)&&(a.charAt(1) >= 48 && a.charAt(1) <= 57)&&(a.charAt(2) >= 48 && a.charAt(2) <= 57)&&(a.charAt(3) == '-')&&(a.charAt(4) >= 48 && a.charAt(4) <= 57)&&(a.charAt(5) >= 48 && a.charAt(5) <= 57)&&(a.charAt(6) == '-')&&(a.charAt(7) >= 48 && a.charAt(7) <= 57)&&(a.charAt(8) >= 48 && a.charAt(8) <= 57)&&(a.charAt(9) >= 48 && a.charAt(9) <= 57)&&(a.charAt(10) >= 48 && a.charAt(10) <= 57))

        {

          System.out.println("Successfully created account for " + first_name + " " + last_name + " Account Number " + num + "\n" + first_name + " " + last_name + ", Balance $" + balance);

        }

        else

        {

          System.out.println("Successfully created account for " + first_name + " " + last_name + ". Inavlid SSN!");

          System.out.println("Successfully created account for " + first_name + " " + last_name + " Account Number " + num);

          System.out.println( first_name + " " + last_name + ", Balance $" + balance);

        }

	}

	public void deposit(float f)

	{

		balance = balance + f;

		System.out.println( first_name + " " + last_name + " deposited " + f + " Current balance $" + balance);

	}

	public void applyInterest()

	{

		balance += ((balance - 10000)*2)/100;

	}

	public void checkBalance()

	{

		System.out.println( first_name + " " + last_name + ", Balance $" + balance);

	}

	public void withdraw(float f)

	{

		if(balance < f)

		{

			System.out.println("Unable to withdraw " + f + " for " + first_name + " " + last_name + " due to insufficient funds");

		}

		else

		{

			balance = balance - f;

			System.out.println( first_name + " " + last_name + " withdrew " + f + ". Current balance $" + balance);

		}

	}

}

