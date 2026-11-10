---
course: "DAA"
semester: 5
tags:
  - course/daa
up: "[[DAA]]"
---

# Suryansh Mithu 
## 24155060
## CSE : 57
## 8.1 Matrix Chain Multiplication — `matrix_chain.c`

```c
#include <stdio.h>
#include <limits.h>
#define MAX 100
void printOptimal(int s[MAX][MAX], int i, int j) {
    if (i == j) {
        printf("A%d", i);
    } else {
        printf("(");
        printOptimal(s, i, s[i][j]);
        printf(" ");
        printOptimal(s, s[i][j] + 1, j);
        printf(")");
    }
}
int main(void) {
    int n;
    int r[MAX], c[MAX], p[MAX + 1];
    int m[MAX][MAX], s[MAX][MAX];
    printf("Enter number of matrices: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of matrices.\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        printf("Enter row and col size of A%d: ", i + 1);
        if (scanf("%d %d", &r[i], &c[i]) != 2) {
            printf("Invalid dimensions.\n");
            return 1;
        }
        if (i > 0 && r[i] != c[i - 1]) {
            printf("Dimension mismatch: A%d columns (%d) != A%d rows (%d)\n",
                   i, c[i - 1], i + 1, r[i]);
            return 1;
        }
    }
    p[0] = r[0];
    for (int i = 0; i < n; i++)
        p[i + 1] = c[i];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            m[i][j] = 0;
            s[i][j] = 0;
        }
    }
    for (int len = 2; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            m[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (q < m[i][j]) {
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }
    printf("\nM Table:\n");
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++)
            printf("%8d", m[i][j]);
        printf("\n");
    }
    printf("\nS Table:\n");
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++)
            printf("%8d", s[i][j]);
        printf("\n");
    }
    printf("\nOptimal parenthesization: ");
    printOptimal(s, 1, n);
    printf("\n");
    printf("The optimal ordering of the given matrices requires %d scalar multiplications.\n",
           m[1][n]);
    return 0;
}
```



```txt

larzival@ubuntu:~/lab8$ gcc -std=c99 matrix_chain.c -o matrix_chain
larzival@ubuntu:~/lab8$ ./matrix_chain
Enter number of matrices: 4
Enter row and col size of A1: 30 35
Enter row and col size of A2: 35 15
Enter row and col size of A3: 15 5
Enter row and col size of A4: 5 10
M Table:
       0   15750    7875    9375
       0       0    2625    4375
       0       0       0     750
       0       0       0       0
S Table:
       0       1       1       3
       0       0       2       3
       0       0       0       3
       0       0       0       0
Optimal parenthesization: ((A1 (A2 A3)) A4)
The optimal ordering of the given matrices requires 9375 scalar multiplications.
```

---

## 8.2 Floyd–Warshall — `floyd_warshall.c`

```
larzival@ubuntu:~/lab8$ cat > inDiAdjMat2.dat <<'EOF'
0 3 8 0 -4
0 0 0 1 7
0 4 0 0 0
2 0 -5 0 0
0 0 0 6 0
EOF
```

---
C program:

```c

#include <stdio.h>
#include <stdlib.h>
#define MAX 100
#define INF 9999
int main(void) {
    int n, u, v;
    int a[MAX][MAX], dist[MAX][MAX], next[MAX][MAX];
    FILE *fp;
    printf("Number of Vertices: ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX) {
        printf("Invalid number of vertices.\n");
        return 1;
    }
    fp = fopen("inDiAdjMat2.dat", "r");
    if (fp == NULL) {
        perror("inDiAdjMat2.dat");
        return 1;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (fscanf(fp, "%d", &a[i][j]) != 1) {
                printf("Error reading matrix from file.\n");
                fclose(fp);
                return 1;
            }
        }
    }
    fclose(fp);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) {
                dist[i][j] = 0;
                next[i][j] = j;
            } else if (a[i][j] != 0) {
                dist[i][j] = a[i][j];
                next[i][j] = j;
            } else {
                dist[i][j] = INF;
                next[i][j] = -1;
            }
        }
    }
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    next[i][j] = next[i][k];
                }
            }
        }
    }
    printf("Shortest distance matrix:\n");
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            printf("%5d", dist[i][j] >= INF ? INF : dist[i][j]);
        }
        printf("\n");
    }
    printf("\nEnter the source and destination vertex: ");
    if (scanf("%d %d", &u, &v) != 2 || u < 1 || u > n || v < 1 || v > n) {
        printf("Invalid source/destination.\n");
        return 1;
    }
    if (next[u][v] == -1) {
        printf("No path from vertex %d to vertex %d.\n", u, v);
    } else {
        printf("Shortest Path from vertex %d to vertex %d: %d", u, v, u);
        int cur = u;
        while (cur != v) {
            cur = next[cur][v];
            printf("-->%d", cur);
        }
        printf("\nPath weight: %d\n", dist[u][v]);
    }
    return 0;
}
```

```

larzival@ubuntu:~/lab8$ gcc -std=c99 floyd_warshall.c -o floyd_warshall
larzival@ubuntu:~/lab8$ ./floyd_warshall
Number of Vertices: 5
Shortest distance matrix:
    0    1   -3    2   -4
    3    0   -4    1   -1
    7    4    0    5    3
    2   -1   -5    0   -2
    8    5    1    6    0
Enter the source and destination vertex: 2 5
Shortest Path from vertex 2 to vertex 5: 2-->4-->1-->5
Path weight: -1
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DAA]] · **Semester:** [[Semester 5]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 5/DAA/Lab/Day4|Day4]] · **Next:** -
> **Related:** [[Data Structures]] · [[Discrete Mathematics]] · [[OOPJ (Java)]]
<!-- connections:end -->
