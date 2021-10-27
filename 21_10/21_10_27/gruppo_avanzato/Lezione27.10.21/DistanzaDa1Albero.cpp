//partendo dal nodo 0, dobbiamo scoprire la distanza di ogni nodo da 0
//il grafo è un ALBERO
#include <bits/stdc++.h>

using namespace std;

int N;
vector<vector<int>> adj;
vector<bool> vis;
vector<int> ans;

void dfs(int x, int dis){
    vis[x] = true;
    ans[x] = dis;
    for (auto k : adj[x]){
        if (!vis[k]){
            dfs(k, dis + 1);
        }
    }
}

int main()
{
    N = 8;
    adj.resize(N);
    vis.resize(N, false);
    ans.resize(N);
    dfs(0, 0);
}