
### 1.

```c
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF 99999

int main()
{
    int n, i, j, s;
    int cost[MAX][MAX];
    int key[MAX];
    int parent[MAX];
    int visited[MAX];
    int totalCost = 0;
    FILE *fp;
    fp = fopen("inUnAdjMat.dat", "r");
    if (fp == NULL) {
        printf("Error: Cannot open file inUnAdjMat.dat\n");
        return 1;
    }
    printf("Enter number of vertices (n): ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) {
     for (j = 1; j <= n; j++) {
    if (fscanf(fp, "%d", &cost[i][j]) != 1) {
     printf("Error: Insufficient data in file.\n");
      fclose(fp);
    return 1;
        }
        }
    }
    fclose(fp);
    printf("\n Input Cost Adjacency Matrix (G) \n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            printf("%5d", cost[i][j]);
        printf("\n");
    }
    printf("\nEnter the starting vertex s (1 to %d): ", n);
    scanf("%d", &s);

    if (s < 1 || s > n) {
        printf("Invalid starting vertex!\n");
        return 1;
    }
    for (i = 1; i <= n; i++) {
        key[i] = INF;
        parent[i] = -1;
        visited[i] = 0;
    }

    key[s] = 0;
    int count;
    for (count = 1; count <= n; count++) {
        int u = -1, minKey = INF;
        for (i = 1; i <= n; i++) {
            if (!visited[i] && key[i] < minKey) {
                minKey = key[i];
                u = i;
            }
        }
        if (u == -1) break;
        visited[u] = 1;
        for (j = 1; j <= n; j++) {
```

```txt
DAA-lab/day7 ❯ ./a.out                                                                                                                                          
Enter number of vertices (n): 6

 Input Cost Adjacency Matrix (G) 
    0    4    0    0    0    0
    0    8    0    4    0    8
    0    0    0    0   11    0
    0    8    0    7    0    4
    0    0    2    0    0    7
    0    9   14    0    0    0

Enter the starting vertex s (1 to 6): 5

 Cost Adjacency Matrix of MST (T)
    0    0    0    0    0    0
    0    0    0    8    0    8
    0    0    0    0   11    0
    0    8    0    0    0    0
    0    0   11    0    0    0
    0    8    0    0    0    0

Edges in MST 
Edge (6 -- 2)  Weight = 8
Edge (5 -- 3)  Weight = 11
Edge (2 -- 4)  Weight = 8
Edge (5 -- 6)  Weight = 0

Total Cost of Minimum Spanning Tree = 27
```


---

### 2.

```c
void unionSets(int parent[], int a, int b) {
    int ra = find(parent, a);
    int rb = find(parent, b);
    parent[ra] = rb;
}

int main()
{
    int n, m, i;
    struct Edge edges[MAX], selected[MAX];
    int parent[MAX];
    int totalCost = 0;
    int edgeCount = 0;
    FILE *fp;

    fp = fopen("UnAdjMat.dat", "r");
    if (fp == NULL) {
        printf("Error: Cannot open file UnAdjMat.dat\n");
        return 1;
    }

    printf("Enter number of nodes and edges (n m): ");
    scanf("%d %d", &n, &m);

    for (i = 0; i < m; i++) {
        if (fscanf(fp, "%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w) != 3) {
            printf("Error: Insufficient data in file.\n");
            fclose(fp);
            return 1;
        }
    }
    fclose(fp);

    for (i = 1; i <= n; i++)
        parent[i] = i;

    sortEdges(edges, m);

    for (i = 0; i < m; i++) {
        int ru = find(parent, edges[i].u);
        int rv = find(parent, edges[i].v);

        if (ru != rv) {
            selected[edgeCount++] = edges[i];
            totalCost += edges[i].w;
            unionSets(parent, edges[i].u, edges[i].v);
        }

        if (edgeCount == n - 1)
            break;
    }

    printf("\nEdge   Cost\n");
    for (i = 0; i < edgeCount; i++) {
        printf("%d--%d   %d\n", selected[i].u, selected[i].v, selected[i].w);
    }

    printf("\nTotal Weight of the Spanning Tree: %d\n", totalCost);

    return 0;
}

```

```
DAA-lab/day7 ❯ ./a.out    
Enter number of nodes and edges (n m): 14 9

Edge   Cost
9--14   1
2--4   1
3--8   2
8--11   3
4--7   3
6--4   3
9--2   4
5--9   4

Total Weight of the Spanning Tree: 21
```