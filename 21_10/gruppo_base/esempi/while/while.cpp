#include<iostream>
using namespace std;

int main()
{
	int a = 1;
	
	while(a != 0)
	{
		cout << "NO\n";
		cin >> a;
	}

	a = 0;
	while(a < 10)
	{
		cout << a << " ";
		a++; //incremento a
	}
	cout << "\n";
}
