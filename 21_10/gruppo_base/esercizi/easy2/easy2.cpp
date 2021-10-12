#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	int S[n];

	for (int i = 0; i < n; i++)
	{
		int a, b;
		cin >> a >> b;
		S[i] = a + b;
	}

	int ans = -1;
	for (int i = 0; i < n; i++)
	{
		if (S[i] % 2 == 0)
		{
			if (S[i] > ans)
			{
				ans = S[i];
			}
		}
	}
	cout << ans << "\n";
}
