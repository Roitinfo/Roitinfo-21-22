#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin >> n;

	int A[n];

	for (int i = 0; i < n; i++)
	{
		cin >> A[i];
	}

	int best = -1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (i != j && best < A[i] + A[j] && (A[i] + A[j]) % 2 == 0)
			{
				best = A[i] + A[j];	
			}
		}
	}
	cout << best << "\n";
}
