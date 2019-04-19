#include <cs50.h>
#include <stdio.h>

/** This program gives the minimum possible number of coins required 
**For any amount of change, which is the input.*/

int main(void)
{
    double input;
    int coins;
    int penny; 
    int quater;
    int nickel;
    int dime;
    int noOfCoins;
    int remainingCoins;
    
    do
    {
        printf("How much change is owed?\n");
        input = get_double();
    }
    while(input < 0);
    
    input = input * 100;
    coins = input;
    quater = coins / 25;
    remainingCoins = coins - (quater * 25);
    dime = remainingCoins / 10;
    remainingCoins = remainingCoins - (dime * 10);
    nickel = remainingCoins / 5;
    remainingCoins = remainingCoins - (nickel * 5);
    penny = remainingCoins;
    noOfCoins = quater + dime + nickel + penny;
    printf("%i\n", noOfCoins);  

}
