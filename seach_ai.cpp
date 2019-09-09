#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;

string state;
map<string, int> seen_states;
map<int, string> id_string;
int ID;
int level[MAXN];
int parent[MAXN];
int max_level = 1;
set<string> levels[MAXN];
string last_state = "123456780";

int getMap(char c) { return (c - '0'); }

vector<vector<int>> getMatriz(string current_state) {
    vector<vector<int>> rep = vector<vector<int>>(3, vector<int>(3, 0));
    int row = 0;
    int col = 0;
    for (int i = 0; i < 9; ++i) {
        rep[row][col] = getMap(current_state[i]);
        col = (col + 1) % 3;
        if (col == 0) row++;
    }
    return rep;
}

string getStringFromMatriz(vector<vector<int>> matriz) {
    string res = "";
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            res += to_string(matriz[i][j])[0];
        }
    }
    return res;
}

pair<int, int> getEmptyCoord(vector<vector<int>> matriz) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (!matriz[i][j]) return {i, j};
        }
    }
    return {-1, -1};
}

int n_x[] = {-1, 1, 0, 0};
int n_y[] = {0, 0, -1, 1};

void BFS(string state_origin) {
    if (seen_states[state_origin] == 0) {
        seen_states[state_origin] = ID++;
        level[seen_states[state_origin]] = 1;
        levels[1].insert(state_origin);
        parent[1] = 1;
        id_string[1] = state_origin;
    }

    queue<string> Q;
    Q.push(state_origin);
    while (!Q.empty()) {
        string current_state = Q.front();
        Q.pop();

        vector<vector<int>> matriz = getMatriz(current_state);
        pair<int, int> pos0 = getEmptyCoord(matriz);
        for (int i = 0; i < 4; ++i) {
            int posx = pos0.second + n_x[i];
            int posy = pos0.first + n_y[i];
            if ((posy < 3) && (posy >= 0) && (posx < 3) && (posx >= 0)) {
                vector<vector<int>> nmatriz = getMatriz(current_state);
                swap(nmatriz[pos0.first][pos0.second],nmatriz[posy][posx]);
                string v = getStringFromMatriz(nmatriz);
                if (seen_states[v] == 0) {
                    seen_states[v] = ID++;
                    level[seen_states[v]] = level[seen_states[current_state]] + 1;
                    max_level = max(max_level, level[seen_states[v]]);
                    levels[level[seen_states[v]]].insert(v);
                    parent[seen_states[v]] = seen_states[current_state];
                    id_string[seen_states[v]] = v;
                    if (v == last_state) return;
                    Q.push(v);
                }
            }
        }

    }
}

void printMatriz(string s) {
    cout << "&&&&&&&&\n";
    for (int i = 0; i < s.size(); ++i) {
        cout << s[i] << ' ';
        if (i % 3 == 2) cout << '\n';
    }
}

int main() {

    string initial_state = "421735086";
    ID++;
    BFS(initial_state);
    for (int i = 1; i <= max_level; ++i) {
        cout << "LEVEL(" << i << ") : " << levels[i].size() << '\n';
    } 
    int search_id = seen_states[last_state];
    int length = 1;
    while (1) {
        cout << length++ << '\n';
        printMatriz(id_string[search_id]);
        if (parent[search_id] == search_id) break;
        search_id = parent[search_id];
    }


    return 0;
}