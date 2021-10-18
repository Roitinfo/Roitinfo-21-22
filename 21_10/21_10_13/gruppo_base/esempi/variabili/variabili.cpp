#include<iostream>
using namespace std;

int main()
{
	int a; //dichiarazione di una variabile intera
	a = 1; //assegnamento di un valore alla variabile
	cout << a << "\n"; //output della variabile
	
	int b = 5; //assegnamento nella dichiarazione (chiamato inizializzazione)
	//b assume subito il valore 5
	int c = a + b; //operazioni con variabili
	//che valore assumerà c?
	cout << c << " " << a - b << "\n"; //output di variabili
	cout << "\n";

	cin >> a; //input di una variabile
	cin >> b >> c; //input di più variabli

	cout << a + b << " " << b - c;
}
