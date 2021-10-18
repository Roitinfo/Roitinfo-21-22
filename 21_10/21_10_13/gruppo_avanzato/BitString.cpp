#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

using namespace std;

main ()
{
	// input
	int N;
	cin >> N;
	// dobbiamo calcolare 2^N, e sappiamo che 2^N = 2*2*2*2... N volte
	int potenza = 1;
	for (int i = 0; i < N; i++){
		potenza *= 2;
		potenza %= 1000000007;
	}
	// output evitando gli errori di c++
	if (potenza < 0){
		potenza += 1000000007;
	}
	cout << potenza;
}

