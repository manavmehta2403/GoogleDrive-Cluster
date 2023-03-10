// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//


#include <iostream>

#include <string>

#include <cctype>

#include <stack>

#include <queue>



using namespace std;



int main()

{

	string input;

	cout << "Enter the string: " << endl;
	getline(cin, input);



	for (int a = 0; a < input.length(); a++)

	{

		input[a] = tolower(input[a]);

	}

	cout << input << endl;

	stack<string> inputStack;

	queue<string> inputQueue;

	inputStack.push(input);

	inputQueue.push(input);



	bool isPalindrome = true;

	for (int a = 0; a < input.length(); a++)

	{

		isPalindrome *= input[a] == input[input.length() - 1 - a];

	}



	if (isPalindrome)

	{

		cout << "This is a palindrome";

	}

	else

	{

		cout << "This is not a palindrome";

	}

	return 0;



}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file