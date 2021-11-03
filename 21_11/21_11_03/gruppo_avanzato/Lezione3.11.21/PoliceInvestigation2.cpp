#include <bits/stdc++.h>

using namespace std;

//la casa che verrà visitata dopo i in posizione i
vector<int> adj;
//conta i nodi visitati prima di questo
vector<int> lastVisit;
//true se il nodo è visitato, false altrimenti
vector<bool> visited;

int dfs(int x, int sum)
{   
    //se è visitato facciamo return della lunghezza del ciclo
    if (visited[x]){
        return (sum - lastVisit[x]);
    }
    //se non è visitato proseguiamo con la dfs
    else{
        visited[x] = true;
        lastVisit[x] = sum;
        return dfs(adj[x], sum + 1);
    }
}

int main()
{   
    /*
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    */

    int N;
    cin >> N;
    adj.resize(N);
    lastVisit.resize(N);
    visited.resize(N, false);

    //carichiamo gli input
    for (int i = 0; i < N; i++){
        cin >> adj[i];
    }

    //ans contiene il valore massimo della lunghezza di un ciclo
    int ans = 0;
    //scorriamo tutti gli elementi fino a che non sono tutti visitati
    for (int i = 0; i < N; i++){
        if (!visited[i]){
            ans = max(dfs(i, 0), ans);
        }
    }

    cout << ans;
    return 0;
}