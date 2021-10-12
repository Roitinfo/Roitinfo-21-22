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

	int par1=-1, par2=-1, dis1=-1, dis2=-1;
	for (int i = 0; i < n; i++)
	{
		if (S[i] % 2 == 1)
		{
			if (dis2 < S[i])
			{
				dis2 = S[i];
			}
			if (dis1 < dis2)
			{
				swap(dis1, dis2);
			}
		}
		else
		{
			if (par2 < S[i])
			{
				par2 = S[i];
			}
			if (par1 < par2)
			{
				swap(par1, par2);
			}
		}
	}

	int ans = -1;
	if (par2 != -1)
	{
		if (ans < par1 + par2)
		{
			ans = par1 + par2;
		}
	}
	if (dis2 != -1)
	{
		if (ans < dis1 + dis2)
		{
			ans = dis1 + dis2;
		}
	}
	cout << ans << "\n";
}
