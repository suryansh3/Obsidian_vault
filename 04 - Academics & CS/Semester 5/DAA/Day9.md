---
course: "DAA"
semester: 5
tags:
  - course/daa
up: "[[DAA]]"
---
```c
#include <stdio.h>
#include <string.h>

#define MAX 1000

int main() {
    char str1[MAX], str2[MAX];
    char lcs[MAX];
    static int dp[MAX + 1][MAX + 1];

    printf("Enter the first string into an array: ");
    scanf("%s", str1);

    printf("Enter the second string into an array: ");
    scanf("%s", str2);

    int n = strlen(str1);
    int m = strlen(str2);

    /* Build LCS DP table */
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = (dp[i - 1][j] > dp[i][j - 1])
                               ? dp[i - 1][j]
                               : dp[i][j - 1];
        }
    }

    /* Reconstruct the LCS */
    int i = n, j = m, index = 0;

    while (i > 0 && j > 0) {
        if (str1[i - 1] == str2[j - 1]) {
            lcs[index++] = str1[i - 1];
            i--;
            j--;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }

    lcs[index] = '\0';

    /* Reverse the LCS string */
    for (int left = 0, right = index - 1; left < right; left++, right--) {
        char temp = lcs[left];
        lcs[left] = lcs[right];
        lcs[right] = temp;
    }

    printf("       LCS: %s\n", lcs);
    printf("       LCS Length: %d\n", dp[n][m]);

    return 0;
}
```

Sample Output:
```text
Enter the first string into an array: 10010101
Enter the second string into an array: 010110110
       LCS: 100110
       LCS Length: 6
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DAA]] · **Semester:** [[Semester 5]] · **Map:** [[MOC]]
> **Prev:** - · **Next:** -
> **Related:** [[Data Structures]] · [[Discrete Mathematics]] · [[OOPJ (Java)]]
<!-- connections:end -->
