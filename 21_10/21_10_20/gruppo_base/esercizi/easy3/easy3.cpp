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

	int p1=-1, p2=-1, d1=-1, d2=-1;
	for (int i = 0; i < n; i++)
	{
		if (A[i] % 2 == 0)
		{
			if (A[i] > p1)
			{
				p2 = p1;
				p1 = A[i];
			}
			else if (A[i] > p2)
			{
				p2 = A[i];
			}
		}
		else
		{
			if (A[i] > d1)
			{
				d2 = d1;
				d1 = A[i];
			}
			else if (A[i] > d2)
			{
				d2 = A[i];
			}
		}
	}
	
	int ans = -1;
	if (p2 != -1) ans = p1 + p2;
	if (d2 != -1 && d1 + d2 > ans) ans = d1 + d2;
	cout << ans << "\n";
}
