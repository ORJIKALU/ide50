// Helper functions for music

#include <cs50.h>
#include <math.h>

#include "helpers.h"
#include <string.h>
#include <stdio.h>

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // get numerator
    int n = atoi(&fraction[0]);
    // get denominator
    int d = atoi(&fraction[2]);
    // if the numerator is 8 then return denominator
    if (d == 8)
    {
       return n;
    }
    // if denominator is less than 8 then multiply d and n by 2 till d is 8
    if( d < 8)
    {
      while ( d != 8)
      {
        d = d * 2;
        n = n * 2;
      }
       return n;
    }
    
    // else keep dividing denominator till it becomes 8 then return numerator
    
    else if ( d > 8)
    {
      while ( d != 8)
      {
        d = d / 2;
        n = n / 2;
      }
       return n;
    }
    return n; 
    
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // check if note is valid
    if(strlen(note) < 2 || strlen(note) > 3)
    {
      return 1;
    }
    int octave4 = 4;
    int F4 = 440;
    int f = 0;
    
    int octave = 0;
    
     //  get natural from note
     char nl = note[1];
     // number of semitones nl is from A
     int n = 0;
     // assign n according to note
     if(nl == 'B')
     {
       n = 2;
     }
     if(nl == 'C')
     {
       n = -9;
     }
     if(nl == 'D')
     {
       n = -7;
     }
     
    if(nl == 'E')
     {
       n = -5;
     }
       
     if(nl == 'F')
     {
       n = -4;
     }
     if(nl == 'G')
     {
       n = -2;
     }
    
   // check for accidentals
   if ( strlen(note) == 3)
   {
     if(strcmp(&note[1],"#")== 0)
     {
       n ++;
     }
     else 
     {
       n--;
     }     
    octave = note[2];
   }
  else
  {
    octave = note[1];
  }
  
  f = round(pow(2, n) * F4);
  if(octave > octave4)
   {
       return (2*(octave - octave4)*f);
   }
   else if (octave < octave4)
   {
       return (f/((octave4 - octave)*2));
   }
 return f;
        
 }
   //Determines whether a string represents a rest

bool is_rest(string s)
{
// if user typed a new line only return true else return false
   
 if( strcmp (s,"\n") )
   {
      return true;
   }
 return false;
}
