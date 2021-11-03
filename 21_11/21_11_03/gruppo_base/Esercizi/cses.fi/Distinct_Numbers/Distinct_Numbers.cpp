#include<iostream>
#include<algorithm>
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
	
	sort(x, x+n);
	int ans = 1;
	for (int i = 1; i < n; i++)
	{
		if (x[i-1] != x[i])
		{
			ans++;
		}
	}
	cout << ans << "\n";
}

