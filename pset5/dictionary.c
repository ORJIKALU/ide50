/****************************************************************************
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 ***************************************************************************/

#include <stdbool.h>
 #include <stdio.h>
#include "dictionary.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


/**
 * Returns true if word is in dictionary else false.
 */


// no of words in the dictionary.
int noOfWords;

// declares a struct node.
typedef struct node
{
	bool value;
    struct node* children[26];
}
node;



node* mainNode;

int getAscii(char letter)
{
	if(letter == '\'')
	{
		return 25;
	}
	else 
	{
    		return (int) tolower(letter) - 'a';
	}
}

void release(node* pointer)
{
	for(int i = 0; i < 26; i++)
	{
		if(i == 25 && pointer -> children[i] == NULL)
		{
			free(pointer);
		}
		else if(pointer -> children[i] != NULL)
		{
			release(pointer -> children[i]);
		}
		
	}
}

// function check if a word is in the dictionary
bool check(const char* word)
{

	
    int n = strlen(word);
	// declares the cursor pointer and points it the hashtable
    node* cursor = mainNode;
	// gets the length of word
    char temp1 [n + 1];
	// copys the word into temp

	strcpy(temp1, word);
	char* temp = temp1;
	
	// loop changes the letters of the word to small letters
    for(int i = 0; i < n; i++)
    {
		 // if letter is a capital letter change to small letter
        if((temp[i] >= 'A') && (temp[i] <= 'Z'))
        {   
            temp[i] = tolower(temp[i]);
        }
	  	int asciiValue = getAscii(temp[i]);
		if(cursor -> children[asciiValue] == NULL)
		{
			return false;
		}
		
		cursor = cursor -> children[asciiValue];
		if(i == (n - 1))
		{
			return cursor -> value;
		}
    }
return false;
	
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    // opens the dictionary and assigns a pointer to it
    FILE* file = fopen(dictionary, "r");
    if(file == NULL)
    {
        printf("couldnt open dictionary");
        return false;
    }
	mainNode = malloc(sizeof(node));
    
    
    while(true)
    {	

		char* current = malloc(LENGTH);

		
		
        if(feof(file))
        {
            break;
        }
		// reads a string from dictionary and stores it in the node
        fscanf(file, "%s", current);
		int n = strlen(current);
		node * cursor =  mainNode;
		for(int i = 0; i < n; i++)
		{
			int asciiValue = getAscii(current[i]);
			if(cursor -> children[asciiValue] == NULL)
			{
				cursor -> children[asciiValue] = malloc(sizeof(node));
			}
			
			cursor = cursor -> children[asciiValue];
			if(i == (n - 1))
			{
				cursor -> value = true;
			}
		}
		noOfWords ++;
        free(current);
      }
    
	// close file
    fclose(file);
	// return true.
    return true;
    
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // returns the no of words
    return noOfWords;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    release(mainNode);
    return true;
}

