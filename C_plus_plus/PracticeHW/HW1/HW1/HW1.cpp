// HW1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
using namespace std;

int* pointer;
void SwapP(int *x, int *y); // Declaring SwapP function
void SwapR(int &x, int &y); // Declaring SwapP function
//void SwapP(int& x, int& y); // Declaring SwapP function

int main()
{
    int VariableA = 10; // Instantiate Variable A
    int VariableB = 20; // Instantiate Variable B

    SwapP(&VariableA, &VariableB);  // Obtain the address of the variables
    //SwapP(VariableA, VariableB);  // Obtain the address of the variables


    cout << "Original Values:"<<"\nVariable A: " << VariableA << "\nVariable B: "<< VariableB;
    cout << "\n---------------------------------------";
    cout << "\nOutput using Pass-By-Pointer"<<"\nThe value of Variable A is now " << VariableA << 
        " and the value of Variable B is now " << VariableB;

    SwapR(VariableA, VariableB);
    cout << "\nSwapping once more using SwapR()" << "\nOutput using Pass-By-Reference" << "\nThe value of Variable A is now " << VariableA <<
        " and the value of Variable B is now " << VariableB;
    cout << "\n---------------------------------------";

}
// Solution by creating two pointers

void SwapP(int *x, int *y) // Creating SwapP Function - takes in pointers
{
  int retain_x = *x;     // assigns value at x to retain_x
  *x = *y;               // assigns value at x with value at y
  *y = retain_x;         // assigns value at retain_x to y
}
void SwapR(int &x, int &y)
{
    int z = x;  // Assign value assigned to reference x to z
    x = y;      // Assign value assigned to data at &y to &x
    y = z;      // Assign value z to &y.
}

// Solution using one pointer
/*
void SwapP(int& x, int& y) // Creating SwapP Function - Grabs address of the two variables
{   
    int retain_x = x;       // Assigns value at address x to retain_x
    pointer = &x;           // Point to address of x
    *pointer = y;           // Assign value of y to x
    pointer = &y;           // Point to address of y
    *pointer = retain_x;    // Assign retained x value to y
}
*/




// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
