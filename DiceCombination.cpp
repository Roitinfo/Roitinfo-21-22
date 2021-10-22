#include <bits/stdc++.h>

using namespace std;

#define mod 1000000007

int main()
{
    int N;
    cin >> N;
    vector<int> comb(N + 1, 0);
    comb[0] = 1;

    for (int i = 0; i <= N; i++){
        for (int j = 1; j <= 6; j++){
            if (j + i <= N){
                comb[i + j] = (comb[i] + comb[i + j]) % mod;
            }
        }
    }

    int ans = comb[N];
    if (ans > 0){
        cout << ans;
    }
    else{
        cout << ans + mod;
    }

    return 0;
}