//calling the essential library
#include<iostream>

//namespace
using namespace std;

//ge_mask method to convert the letter of the string into the number
int get_mask(string word,char letter)
{
   int appears = 0;
   for(int i=0;i<word.length();i++)
   {
       if(word[i] == letter)
	   {
           //Using the bitwise OR operator and SHIFT LEFT operator
           //to form the binary number
           //The power at every index of i will be 2*(len-i-1)
           appears = appears | (1 << (word.length() - i - 1));
       }
   }
   return appears;
}

//update method
void update_mask(string word,string &mask,char letter)
{
   //Return if the lengths are not equal
   if(word.length() != mask.length())
    {
    	return;
	} 
	
   int position = get_mask(word,letter);
   
   //the case when the number is 0 for the letter in the string
   if(position == 0)
    {
    	return;
	}   
	
	//calculating the index by subtracting 1 from the length	
    int index = mask.length() - 1;
   
   //when the position is not equal to 0
   while(position!=0)
   {
       //If the current bit is 1, then if it is ? in the mask string
       //then we can insert the letter at that index.
       if(position & 1)
	   {
	   	    //placing the question mark for every letter	
            if(mask[index] == '?')
            {
			    
			   mask[index] = letter;
			}
       }
       //moving the index backwards
       index--;
       //BITWISE RIGHT SHIFT operator at every position
       position = position >> 1;
   }
}

//boolean to get the guessed value
bool guessed(string word, string mask)
{
	//when the mask length and the word length doesn't match
    if(word.length() != mask.length())
    {
       return false;
	}
   //In case all the corresponding letters are same, then return true
   //else return false  
   for(int i=0;i<word.length();i++)
   {
       if(word[i] != mask[i])
        {
			return false;
		}
   }
   return true;
}

//main method
int main()
{
	//setting the word as abcfab		
    string word = "abcfab";
    //setting the mask as "??c???"
    string mask = "??c???";
    
    //geting the index number for the letters in the string
    cout<<"get_mask(word,'a') = "<<get_mask(word,'a')<<endl;
    cout<<"get_mask(word,'e') = "<<get_mask(word,'e')<<endl;
    cout<<"get_mask(word,'f') = "<<get_mask(word,'f')<<endl;
    cout<<"get_mask(word,'b') = "<<get_mask(word,'b')<<endl;
    
    //updating the mask for every letter that is in the string
    mask = "??c???";
    update_mask(word, mask,'e');
    cout<<"update_mask(word, mask,'e') = "<<mask<<endl;
    //checking if the string and mask is equal
    cout<<"bool guessed(word, mask):{0 for false 1 for true}: "<<guessed(word,mask)<<"\n";
    mask = "??c???";
    update_mask(word, mask,'a');
    cout<<"update_mask(word, mask,'a') = "<<mask<<endl;
    //again checking the whether they are equal or not
    cout<<"bool guessed(word, mask):{0 for false 1 for true}: "<<guessed(word,mask)<<"\n";
    update_mask(word, mask,'f');
    cout<<"update_mask(word, mask,'f') = "<<mask<<endl;
    //same step 
    cout<<"bool guessed(word, mask):{0 for false 1 for true}: "<<guessed(word,mask)<<"\n";
    update_mask(word, mask,'b');
    cout<<"update_mask(word, mask,'b') = "<<mask<<endl;
    //1 is for being true when word and mask is equal
    cout<<"bool guessed(word, mask):{0 for false 1 for true}: "<<guessed(word,mask)<<"\n";
    
}
