//partendo dal nodo 0, dobbiamo scoprire la distanza di ogni nodo da 0
//il grafo è un grafo qualsiasi
#include <bits/stdc++.h>

using namespace std;

int N;
vector<vector<int>> adj;
vector<bool> vis;
vector<int> ans;

int main()
{
    N = 8;
    adj.resize(N);
    vis.resize(N, false);
    ans.resize(N);
    //nella queue in prima posizione mettiamo il nodo e in seconda la sua distanza
    queue<pair<int, int>> q;
    q.push({0, 0});
    while (!q.empty()){
        int t = q.front().first;
        int dis = q.front().second;
        vis[t] = true;
        ans[t] = dis;
        for (auto k : adj[t]){
            if (!vis[k]){
                q.push({k, dis + 1});
            }
        }
     	q.pop();
    }
}
