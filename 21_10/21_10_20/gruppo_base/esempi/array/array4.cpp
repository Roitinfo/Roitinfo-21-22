#include<iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int A[n];
	for (int i = 0; i < n; i++)
	{
		cin >> A[i];
	}

	//stampo le somme di tutte le coppie possibili prese nella sequenza
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << A[i] + A[j] << " ";
		}
		cout << "\n";
	}
}
