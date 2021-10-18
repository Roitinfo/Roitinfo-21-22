#include<iostream>
using namespace std;

int main()
{
	int S[10]; //dichiarazione di un array di lunghezza 10
	S[0] = 2; //i valori dell'array si comportano come variabili
	S[1] = 3;
	cout << S[0] << " " << S[0] + S[1] << "\n";

	cin >> S[2]; //si possono anche prendere in input
	cout << S[2] - S[1] << "\n";
}
