#include<iostream>
using namespace std;

int main()
{
	int S[10];
	//riempimento dell'array con un valore costante (nell'esempio: 5)
	for (int i = 0; i < 10; i++)
	{
		S[i] = 5; 
	}
	//ora tutte le posizioni dell'array contengono 5

	//calcolo la somma di tutti i valori nell'array
	int sum = 0; //usando una variabile aggiuntiva
	for (int i = 0; i < 10; i++)
	{
		sum = sum + S[i];
	}
	cout << sum << "\n"; //50
}
