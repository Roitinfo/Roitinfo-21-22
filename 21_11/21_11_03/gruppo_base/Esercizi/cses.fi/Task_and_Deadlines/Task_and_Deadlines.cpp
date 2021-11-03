#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
 	int n;
 	cin >> n;
 	int a[n], d[n];
 	for (int i = 0; i < n; i++)
 	{
 		cin >> a[i] >> d[i];
	}
	
	long long ans = 0;
	for (int i = 0; i < n; i++)
	{
		ans += d[i];
	}
	
	sort(a, a+n);
	long long t = 0;
	for (int i = 0; i < n; i++)
	{
		t += a[i];
		ans -= t;
	}
	cout << ans << "\n";
}

