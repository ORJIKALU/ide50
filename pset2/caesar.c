/**
*This program takes in an int say n as a commandline argument
*It then asks the user for a line of text 
*It then changes each character in the text to the nth character 
*according to the order of the English alphabet
*counting from that particular character
*if the shift exceeds 'z' then counting continues from 'a'.
*it also retains the case of the character
*and prints non alphabetic character without shifting it.
*/
#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int main (int argc, string argv[])
{
    // checks whether the commandline argument is given and correctly
    // else it returns one and quits
    if(argc != 2)
    {
        printf("Usage: /home/cs50/pset2/caesar <key>\n");
        return 1;
    }
    else
    {
       
        printf("");
        //asks the user for input
        string input;
        // for keeping users input
        input = GetString();
        int key;
        // holds the value of the key
        key = atoi(argv[1]);
        key = key % 26;
        //wrap key around 26 incase it is greater than 26.
        int p;
        int c;
        int num;
        // num holds the equivalent ascii integer for the alphabet.
        int sum;
        for (int i = 0;i < strlen(input); i++)
        {
            if (('A' - 1) < input[i] && input[i] < ('Z' + 1))
            {
                num = (int)input[i];
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
    
    
    
}
