#include<iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	//programma che conta da 0 a n-1
	for (int i = 0; i < n; i++)
	{
		cout << i << " ";
	}
	cout << "\n";

	/*
	più semplice di

	int n;
	cin >> n;
	int i = 0;
	while(i < 10)
	{
		cout << i << " ";
		i++;
	}
	cout << "\n";
	*/
}
