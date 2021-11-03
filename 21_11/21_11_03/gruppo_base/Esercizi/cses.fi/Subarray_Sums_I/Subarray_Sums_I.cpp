#include<iostream>
using namespace std;

int main()
{
 	int n, x;
 	cin >> n >> x;
 	int t[n];
 	for (int i = 0; i < n; i++)
 	{
 		cin >> t[i];
	}
	
	long long sum = 0;
	int ans = 0;
	int i = 0;
	for (int j = 0; j < n; j++)
	{
		sum += t[j];
		while(sum > x)
		{
			sum -= t[i];
			i++;
		}
		if (sum == x)
		{
			ans++;
		}
	}
	cout << ans << "\n";
}

