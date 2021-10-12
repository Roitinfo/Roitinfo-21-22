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
		cin >> S[i];
	}

	int ans = -1000;
	for (int i = 0; i < n; i++)
	{
		if (S[i] > ans)
		{
			ans = S[i];
		}
	}
	cout << ans << "\n";
}
