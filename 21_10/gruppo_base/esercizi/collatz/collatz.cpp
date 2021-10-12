#include<iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	int count = 1;

	while(n != 1)
	{
		count++;
		if (n % 2 == 1)
		{
			n = n * 3 + 1;
		}
		else
		{
			n = n / 2;
		}
	}
	cout << count << "\n";
}
