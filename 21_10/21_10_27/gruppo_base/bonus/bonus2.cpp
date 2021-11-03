#include<iostream>
using namespace std;

int main()
{
 	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin >> N;
	int A[N], B[N];
	int num=0, den=0;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i] >> B[i];
		num += A[i];
		den += B[i];
	}
	
	int bnum = num, bden = den;
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		int cnum = num - A[i];
		int cden = den - B[i];
		if (cnum * bden > bnum * cden)
		{
			ans = i;
			bnum = cnum;
			bden = cden;
		}
	}
	cout << ans;
}

