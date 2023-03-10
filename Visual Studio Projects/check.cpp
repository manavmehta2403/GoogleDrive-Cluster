#include <iostream>
using namespace std;

int main() {
    for (;;) {
        int m, n, i, j;
        cin >> m >> n;
        if (m == 0 && n == 0)
            break;
        char ch[m][n];
        for (i = 0; i < m; i++) {
            for (j = 0; j < n; j++) {
                char c;
                cin >> c;
                ch[i][j] = tolower(c);
            }
        }
        int test;
        cin >> test;
        while (test--) {
            string str;
            cin >> str;
            int ctr = 0;
            for (i = 0; i < m; i++) {
                for (j = 0; j < n; j++) {
                    if (ch[i][j] == tolower(str[0])) {
                        if (ch[i][j - 1] == tolower(str[1]) && ch[i][j - 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i - 1][j - 1] == tolower(str[1]) && ch[i - 2][j - 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i - 1][j] == tolower(str[1]) && ch[i - 2][j] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i - 1][j + 1] == tolower(str[1]) && ch[i - 2][j + 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i][j + 1] == tolower(str[1]) && ch[i][j + 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i + 1][j + 1] == tolower(str[1]) && ch[i + 2][j + 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i + 1][j] == tolower(str[1]) && ch[i + 2][j] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                        if (ch[i + 1][j - 1] == tolower(str[1]) && ch[i + 2][j - 2] == tolower(str[2])) {
                            ctr = -1;
                            cout << i + 1 << " " << j + 1 << endl;
                            break;
                        }
                    }
                }
                if (ctr < 0)
                    break;
            }
        }
    }
    return 0;
}
