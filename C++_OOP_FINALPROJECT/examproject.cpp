#include <iostream>
using namespace std;

struct Denomination {
    int value;  
    int count;  
};

const int SIZE = 3; 
void sortDescending(Denomination denoms[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            if (denoms[i].value < denoms[j].value) {
                Denomination temp = denoms[i];
                denoms[i] = denoms[j];
                denoms[j] = temp;
            }
        }
    }
}

bool dispenseCash(Denomination denoms[], int amount) {
    sortDescending(denoms); 

    cout << "\nDispensing amount: " << amount << endl;

    for (int i = 0; i < SIZE; i++) {
        while (amount >= denoms[i].value && denoms[i].count > 0) {
            amount -= denoms[i].value;  
            denoms[i].count--;          
            cout << "  Dispensed: " << denoms[i].value << endl;
        }
    }

    if (amount == 0) {
        cout << "Successfully dispensed full amount.\n";
        return true;
    } else {
        cout << "Cannot dispense full amount. Remaining: " << amount << endl;
        return false;
    }
}

int main() {
    Denomination denoms[SIZE]; 

    for (int i = 0; i < SIZE; i++) {
        cout << "Enter denomination value #" << (i + 1) << ": ";
        cin >> denoms[i].value;
        cout << "Enter count for " << denoms[i].value << ": ";
        cin >> denoms[i].count;
    }

    int amount;
    cout << "\nEnter amount to withdraw: ";
    cin >> amount;

    dispenseCash(denoms, amount);

    return 0; 
}

