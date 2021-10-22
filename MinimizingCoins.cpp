#include <bits/stdc++.h>

using namespace std;

#define mod 1000000007
#define inf 1000001

int main()
{
    int N, target;
    cin >> N >> target;
    vector<int> monete(N);
    for (int i = 0; i < N; i++){
        cin >> monete[i];
    }

    vector<int> comb(target + 1, inf);
    comb[0] = 0;
    for (int i = 0; i < target; i++){
        for (int j = 0; j < N; j++){
            if (i + monete[j] <= target){
                if (comb[i] + 1 < comb[i + monete[j]]){
                    comb[i + monete[j]] = comb[i] + 1;
                }
            }
        }   
    }

    if (comb[target] == inf){
        cout << -1;
    }
    else{
        cout << comb[target];
    }

    return 0;
}