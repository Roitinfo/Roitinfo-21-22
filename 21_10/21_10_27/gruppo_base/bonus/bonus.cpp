#include<iostream>
using namespace std;

int main()
{
 	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin >> N;
	int A[N], B[N];
	double num=0, den=0;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i] >> B[i];
		num += A[i];
		den += B[i];
	}
	
	double tot = num/den;
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		double val = (num - A[i])/(den - B[i]);
		if (val > tot)
		{
			ans = i;
			tot = val;
		}
	}
	cout << ans;
}

