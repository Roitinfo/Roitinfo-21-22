#include<iostream>
using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	int S[n];
	
	for (int i = 0; i < n; i++)
	{
		cin >> S[i];
	}
	
	int ans = -1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (i != j && (S[i] + S[j]) % 2 == 0 && S[i] + S[j] > ans)
			{
				ans = S[i] + S[j];
			}
		}
	}
	cout << ans;
}
