#include <bits/stdc++.h>

using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<long long int> numbers(N);
    long long int maximum = -100000000;
    for (int i = 0; i < N; i++){
        cin >>  numbers[i];
        maximum = max(maximum, numbers[i]);
    }

    long long int ans = 0, sum = 0;
    long long int k = 0;
    for (int i = 0; i < N; i++){
        sum = max(k, sum + numbers[i]);
        ans = max(ans, sum);
    }

    if (ans){
        cout << ans;
    }
    else{
        cout << maximum;
    }

    return 0;
}