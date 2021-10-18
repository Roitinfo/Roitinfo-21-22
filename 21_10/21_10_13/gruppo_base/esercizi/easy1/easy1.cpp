#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;

	int ans = -1000;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		if (a > ans)
		{
			ans = a;
		}
	}
	cout << ans << "\n";
}
