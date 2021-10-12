#include<iostream>
using namespace std;

int main()
{
	int S[10]; //dichiarazione di un array di lunghezza 10
	S[0] = 2; //i valori dell'array si comportano come variabili
	S[1] = 3;
	cout << S[0] << " " << S[0] + S[1] << "\n";

	cin >> S[2];
	cout << S[2] - S[1] << "\n";

	//cout << S[10000] << "\n"; //ERRATO, non fatelo

	for (int i = 0; i < 10; i++)
	{
		S[i] = 5; 
	}

	int sum = 0;
	for (int i = 0; i < 10; i++)
	{
		sum = sum + S[i];
	}
	cout << sum << "\n";

	for (int i = 0; i < 5; i++)
	{
		cin >> S[i];
	}

	int sum = 0;
	for (int i = 0; i < 10; i++)
	{
		sum = sum + S[i];
	}
	cout << sum << "\n";
}
