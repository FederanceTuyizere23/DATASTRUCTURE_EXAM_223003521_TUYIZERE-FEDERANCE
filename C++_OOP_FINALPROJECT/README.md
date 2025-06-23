C++_OOP_FINALPROJECT/README.md


# C-IN-OOP-EXAM_HUYE_223003521_TUYIZERE-FEDERANCE



**ATM CASH DISPENSER SIMUATION**


**TASK OVERVIEW**

The job was to create a C++ program that simulates an ATM cash dispenser. It should:
Let users enter different currency types and how many notes of each are available.
Take in an amount the user wants to withdraw.
Try to give out that amount using the available notes, starting with the biggest ones.
Show which notes were given out.
Let the user know if the exact amount can't be dispensed.
This project covers basic programming ideas like structures, arrays, sorting, loops, conditionals, and functions in C++.


**HOW IT WAS DONE/COMPLETED**

To get this done:
A `Denomination` struct was made to hold the note values and their counts.
A constant integer `SIZE` was set to keep track of how many denominations there are.
The `sortDescending` function was added to sort the denominations from highest to lowest so the biggest notes come out first.
The main cash dispensing logic is found in `dispenseCash`:
It goes through the sorted denominations and dispenses notes as long as it can.
It updates the amount left to dispense and the number of notes available.
It prints each note given out.
It tells whether the full amount was dispensed or not.
The `main` function gathers what the user inputs for the denominations, their counts, and the amount to withdraw.
Finally, it calls the dispensing function and shows the results.


**CODE EXPLANATION**


**#include <iostream>**

Includes the input/output stream library needed for console I/O.


**using namespace std;**

Avoids needing to prefix std:: before common functions like cout and cin.


**struct Denomination {**

Defines a structure to hold information about each note: its value and count.


**int value;**

Note value (ex, 100, 50).


**int count;**

Number of such notes available.


**};**

End of struct definition.


**const int SIZE = 3;**

Sets the number of denominations to be handled to 3.


**void sortDescending(Denomination denoms[]) {**

Declares a function to sort the array of denominations in descending order by their value.


**for (int i = 0; i < SIZE - 1; i++) {**

Outer loop for selection sort. Iterates through elements.


**for (int j = i + 1; j < SIZE; j++) {**

Inner loop compares current element with next elements.


**if (denoms[i].value < denoms[j].value) {**

If current value is less, swap to bring larger value forward.


**Denomination temp = denoms[i];**

Temporary variable to hold current element.


**denoms[i] = denoms[j];**

Swap elements.


**denoms[j] = temp;**

Complete the swap.


**}**

End of if condition.


**}**

End of inner loop.


**}**

End of outer loop.


**}**

End of sorting function.


**bool dispenseCash(Denomination denoms[], int amount) {**

Function attempts to dispense the requested amount. Returns true if successful.


**sortDescending(denoms);**

Sort denominations from highest to lowest.


**cout << "\nDispensing amount: " << amount << endl;**

Prints the amount to withdraw.


**for (int i = 0; i < SIZE; i++) {**

Iterate over each denomination.


**while (amount >= denoms[i].value && denoms[i].count > 0) {**

Dispense notes while possible.


**amount -= denoms[i].value;**

Reduce amount by note value.


**denoms[i].count--;**

Decrease available note count.


**cout << "  Dispensed: " << denoms[i].value << endl;**

Print the dispensed note.


**}**

End dispensing loop for this denomination.


**}**

End denomination loop.


**if (amount == 0) {**

Check if full amount dispensed.


**cout << "Successfully dispensed full amount.\n";**

Print success message.


**return true;**

Return success.


**} else {**

If amount remains.


**cout << "Cannot dispense full amount. Remaining: " << amount << endl;**

Print failure message.


**return false;**

Return failure.


**}**

End if-else.


**}**

End dispenseCash function.


**int main() {**

Main program execution starts here.


**Denomination denoms[SIZE];**

Declare array of denominations.


**for (int i = 0; i < SIZE; i++) {**

Loop to get user input.


**cout << "Enter denomination value #" << (i + 1) << ": ";**

Prompt for denomination value.


**cin >> denoms[i].value;**

Read denomination value.


**cout << "Enter count for " << denoms[i].value << ": ";**

Prompt for note count.


**cin >> denoms[i].count;**

Read note count.


**}**

End input loop.


**int amount;**

Declare variable for withdrawal amount.


**cout << "\nEnter amount to withdraw: ";**

Prompt for amount.


**cin >> amount;**

Read amount.


**dispenseCash(denoms, amount);**

Call function to dispense cash.


**return 0;**

End program.


**}**

End main function




