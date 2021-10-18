#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

using namespace std;

main ()
{
	//input
	int N, M, K;
	cin >> N >> M >> K;
	vector<int> persone(N), appartamenti(M);
	for (int i = 0; i < N; i++){
		cin >> persone[i];
	}
	for (int i = 0; i < M; i++){
		cin >> appartamenti[i];
	}
	//sortiamo le persone e le case
	sort(persone.begin(), persone.end());
	sort(appartamenti.begin(), appartamenti.end());
	//usiamo un ciclo while per scorrere contemporaneamente i due vettori
	int ans = 0;
	int i = 0, j = 0;
	while(i < N && j < M){
		int p = persone[i], a = appartamenti[j];
		//persona e appartamento sono compatibili
		if (a >= p - K && a <= p + K){
			ans++;
			i++;
			j++;
		}
		//persona è minore
		else if (a > p + K){
			i++;
		}
		//appartamento è minore
		else if (a < p - K){
			j++;
		}
	}
	//output
	cout << ans;
}

