#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin); //utilizzo per l'input: freopen("nomefile", "r", stdin);
	freopen("output.txt", "w", stdout); //utilizzo per l'output: freopen("nomefile", "w", stdout);
	/*
	programma di esempio, che legge 3 numeri da un file e ne scrive il prodotto su un altro file 
	UTILIZZO: nella stessa cartella di questo programma, creare un file nominato input.txt, contenente 3 interi separati da uno spazio
	*/
	int a, b, c;
	cin >> a >> b >> c;
	int d = a * b * c;
	cout << d << "\n";
}
