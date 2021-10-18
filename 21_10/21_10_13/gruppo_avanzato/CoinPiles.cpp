#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

using namespace std;

main ()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		// input
		int A, B;
		cin >> A >> B;
		// ci assicuriamo che A > B
		if (B > A){
			swap(A, B);
		}
		// portiamo entrambe le torri alla stessa altezza
		int altezza = A - 2 * (A - B);
		// verifichiamo che altezza è divisibile per tre
		if (altezza >= 0 && altezza % 3 == 0){
			cout << "YES";
		}
		else{
			cout << "NO";
		}
		cout << "\n";
	}
}

