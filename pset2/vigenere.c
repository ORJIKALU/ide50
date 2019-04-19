#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int main (int argc, string argv[])
{  
    // if the commandline argument is not given or more than 2 return 1
    if(argc != 2)
        {
            printf("key should not contain non alphabetic characters\n");
            return 1;
        } 
        
    // Assign the length of the key to n.
    int n = strlen(argv[1]);
    // defines an array of chars that stores the characters in the key.   
    char keyArray[n];
    // Assigns the characters in the command line argument to the character Array
    for(int i = 0; i < n; i++)
    {
        keyArray[i] = argv[1][i];   
        // checks all the characters in the commandline argument 
        //if any of the characters is not an alphabetic character
        // it ends the program returning i as a sentinal.
        if(!(((('A' - 1) < argv[1][i] && argv[1][i] < ('Z' + 1))) || ((('a' - 1) < argv[1][i] && argv[1][i] < ('z' + 1)))))
        {
            printf("Usage: /home/cs50/pset2/caesar <key>\n");
            return 1;
        }
        
    }
    // defines an array of integers to hold the integer value of key characters
    int keyNumbers[n];
    printf("");
    string input = GetString();
    int j = 0;
    int m = strlen(input);
    int p;
    int c;
    int num;
    // num holds the equivalent ascii integer for the alphabet.
    int sum;
    int key;
    for (int i = 0; i < n; i++)
    {
        if (('A' - 1) < keyArray[i] && keyArray[i] < ('Z' + 1))
        {
            keyNumbers[i] = (int)keyArray[i] - 'A';
            
        }
        else if (('a' - 1) < keyArray[i] && keyArray[i] < ('z' + 1))
            keyNumbers[i] = (int)keyArray[i] - 'a';
    }
   
    for (int i =0;i < m; i++)
        {
            if (('A' - 1) < input[i] && input[i] < ('Z' + 1))
            {

                num = (int)input[i];
                j = j % n;
                key = keyNumbers[j];
                j++;
               
                // assigns the number value of the character according to ascii.
                sum = num + key;
                if (sum > 'Z')
                {
                    p = num - 'A';
                    // returns the integer value to that of A.
                    c = (p + key) % 26;
                    // c becomes the new key and rotation starts from A.
                    printf("%c", ('A' + c));
                }
                else
                    printf("%c", (input[i] + key));
                
            }
            else if (('a' - 1) < input[i] && input[i] < ('z' + 1))
            {
                num = (int)input[i];
                // assigns the number value of the character according to ascii.
                j = j % n ;
                key = keyNumbers[j];
                j++;
                sum = num + key;
                if (sum > 'z')
                {
                    p = num - 'a';

                    // returns the integer value to that of A.
                    c = (p + key) % 26;
                    // c becomes the new key and rotation starts from A.
                    printf("%c", ('a' + c));
                }
                else
                    printf("%c", (input[i] + key));
                
            }
            else
            {
                printf("%c", input[i]);
            }
                
        }
        printf("\n");  
}
