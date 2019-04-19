#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf ("Please enter ./vigenere followed by a keyword\n");
        return 1;
    }

    else
    {
        printf ("");
    }

    for (int a = 0, b = strlen(argv[1]); a < b; a++)
    {
        if (isdigit (argv[1][a]))
        {
            printf ("Keyword must be all alphabets(uppercase and/or lowercase).\n");
            return 1;
        }
    }

    int cipher = 0;
    string text = GetString ();

    int e = 0;
    int f = strlen(argv[1]);
    for (int c = 0, d = strlen(text); c < d; c++)
    {
        
            if (isupper (text[c]))
            {
                if (isupper (argv[1][e]))
                {
                    cipher = (((int) text[c] - 65) + ((int) argv[1][e] - 65)) % 26;
                    printf ("%c", (char) cipher + 65);
                }

                else if (islower (argv[1][e]))
                {
                    cipher = (((int) text[c] - 65) + ((int) argv[1][e] - 97)) % 26;
                    printf ("%c", (char) cipher + 65);
                }
                if(e < f)
                {
                    e = e + 1;
                }
                else
                {
                    e = 0;
                }
            }

            else if (islower (text[c]))
            {
                if (isupper (argv[1][e]))
                {
                    cipher = (((int) text[c] - 97) + ((int) argv[1][e] - 65)) % 26;
                    printf ("%c", (char) cipher + 97);
                }

                else if (islower (argv[1][e]))
                {
                    cipher = (((int) text[c] - 97) + ((int) argv[1][e] - 97)) % 26;
                    printf ("%c", (char) cipher + 97);
                }
                if(e == (f - 1))
                {
                    e = 0;
                }
                else 
                {
                    e =  e + 1;
                } 
            }

            else
            {
                printf ("%c", text[c]);
            }
           

    }

    printf ("\n");
}
