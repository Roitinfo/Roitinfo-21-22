#include<iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;

	if (a < b)
	{
		cout << "MINORE\n";
	}
	else if (a > b) //se a non è minore di b, controllo se è maggiore
	{
		cout << "MAGGIORE\n";
	}
	else //se non è maggiore (e non è minore), allora a è uguale a b
	{
		cout << "UGUALE\n";
	}
	cout << "\n";

	if (a + b > 0)
	{
		cout << "SOMMA POSITIVA\n";
	}
	cout << "\n";

	if (a % 2 == 0)
	{
		cout << "PARI\n";
	}
	cout << "\n";

	/*
	if (a > 0)
	{
		if (a % 3 == 0)
		{
			"MULTIPLO DI 3 POSITIVO\n";
		}
	}
	cout << "\n";
	*/

	if ((a > 0) && (a % 3 == 0))
	{
		cout << "MULTIPLO DI 3 POSITIVO\n";
	}
}
