#include<iostream>
using namespace std;

int main()
{
 	int n;
 	cin >> n;
 	int x[n];
 	for (int i = 0; i < n; i++)
 	{
 		cin >> x[i];
	}
	
	long long sum = x[0];
	long long ans = sum;
	for (int i = 1; i < n; i++)
	{
		if (sum < 0)
		{
			sum = 0;
		}
		sum += x[i];
		if (sum > ans)
		{
			ans = sum;
		}
	}
	cout << ans << "\n";
}

