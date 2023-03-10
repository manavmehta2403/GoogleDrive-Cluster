/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

public class Sequence {

	private static int eff = 0;
	private static int twoTimes = 2;

	/*
	 * Constructor to initialize instance variable eff
	 */
	public Sequence() {
		eff = 0;
	}

	/**
	 * Computes nth term either recursive or iteratively, where the nth term is twice the previous
	 * number add the next previous number
	 */
	// Method to compute the number using iteration

	public static int computeIterative(int num)

	{

		int result = 0;
		eff = 0;

		// case when number is zero
		if (num == 0) {
			result = 0;
		}

		// case when number is zero
		else if (num == 1) {
			result = 1;
		}

		else {
			int secondPrevious = 0;
			int firstPrevious = 1;

			for (int i = twoTimes; i <= num; i++) {
				eff++;
				// Calculating the result
				result = twoTimes * firstPrevious + secondPrevious;

				// Swapping
				secondPrevious = firstPrevious;

				firstPrevious = result;

			}

		}

		return result;

	}

	// Method to compute the number using recursion
	public static int computeRecursive(int num)

	{

		int result;

		eff++;

		if (num == 0)

		{
			// case when number is zero
			result = 0;

		} else if (num == 1)

		{
			// case when number is zero
			result = 1;

		} else

		{
			// recursion function is called
			result = twoTimes * computeRecursive(num - 1) + computeRecursive(num - 2);

		}

		return result;

	}

	/**
	 * Returns the values (either recursion or the iterative) of the efficiency counter
	 */
	public static int getEfficiency() {
		return eff;
	}

}