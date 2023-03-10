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
