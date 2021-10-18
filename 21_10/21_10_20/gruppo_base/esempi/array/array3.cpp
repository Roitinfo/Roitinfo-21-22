#include<iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int S[n]; //array con lunghezza presa in input

	//input di un array intero
	for (int i = 0; i < n; i++)
	{
		cin >> S[i];
	}
	
	//calcolo la somma dei valori inseriti
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum = sum + S[i];
	}
	cout << sum << "\n";
}
