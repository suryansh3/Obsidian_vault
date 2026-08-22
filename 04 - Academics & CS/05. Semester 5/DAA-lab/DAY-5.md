### 5.1 Fractional Knapsack

```c
#include <stdio.h>
#include <stdlib.h>

struct ITEM {
    int item_id;
    float item_profit;
    float item_weight;
    float profit_weight_ratio;
};

void heapify(struct ITEM arr[], int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left].profit_weight_ratio < arr[smallest].profit_weight_ratio)
        smallest = left;
    if (right < n && arr[right].profit_weight_ratio < arr[smallest].profit_weight_ratio)
        smallest = right;

    if (smallest != i) {
        struct ITEM temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
        heapify(arr, n, smallest);
    }
}

void heapSort(struct ITEM arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        struct ITEM temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

int main() {
    int n;
    printf("Enter the number of items: ");
    scanf("%d", &n);

    struct ITEM items[n];

    for (int i = 0; i < n; i++) {
        printf("Enter the profit and weight of item no %d: ", i + 1);
        scanf("%f %f", &items[i].item_profit, &items[i].item_weight);
        items[i].item_id = i + 1;
        items[i].profit_weight_ratio = items[i].item_profit / items[i].item_weight;
    }

    float capacity;
    printf("Enter the capacity of knapsack:");
    scanf("%f", &capacity);

    heapSort(items, n);

    printf("%-9s %-16s %-16s %s\n", "Item No", "profit", "Weight", "Amount to be taken");

    float remaining = capacity;
    float total_profit = 0.0;

    for (int i = 0; i < n; i++) {
        float amount;

        if (items[i].item_weight <= remaining) {
            amount = 1.0;
            remaining -= items[i].item_weight;
            total_profit += items[i].item_profit;
        } else if (remaining > 0) {
            amount = remaining / items[i].item_weight;
            total_profit += items[i].item_profit * amount;
            remaining = 0.0;
        } else {
            amount = 0.0;
        }

        printf("%-9d %-16.6f %-16.6f %f\n", items[i].item_id, items[i].item_profit, items[i].item_weight, amount);
    }

    printf("Maximum profit: %f\n", total_profit);
    return 0;
}
```

output:

```text
Enter the number of items: 3
Enter the profit and weight of item no 1: 27 16
Enter the profit and weight of item no 2: 14 12
Enter the profit and weight of item no 3: 26 13
Enter the capacity of knapsack:18
Item No   profit          Weight          Amount to be taken
3         26.000000       13.000000       1.000000
1         27.000000       16.000000       0.312500
2         14.000000       12.000000       0.000000
Maximum profit: 34.437500
```

---

### 5.2 Huffman Coding

```c
#include <stdio.h>
#include <stdlib.h>

struct SYMBOL {
    char alphabet;
    int frequency;
    struct SYMBOL *left;
    struct SYMBOL *right;
};

struct SYMBOL* createNode(char alphabet, int frequency) {
    struct SYMBOL* node = (struct SYMBOL*)malloc(sizeof(struct SYMBOL));
    node->alphabet = alphabet;
    node->frequency = frequency;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void minHeapify(struct SYMBOL** heap, int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && heap[left]->frequency < heap[smallest]->frequency)
        smallest = left;
    if (right < n && heap[right]->frequency < heap[smallest]->frequency)
        smallest = right;

    if (smallest != i) {
        struct SYMBOL* temp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = temp;
        minHeapify(heap, n, smallest);
    }
}

struct SYMBOL* extractMin(struct SYMBOL** heap, int* n) {
    struct SYMBOL* min = heap[0];
    heap[0] = heap[*n - 1];
    (*n)--;
    minHeapify(heap, *n, 0);
    return min;
}

void insertMinHeap(struct SYMBOL** heap, int* n, struct SYMBOL* node) {
    heap[*n] = node;
    (*n)++;
    int i = *n - 1;

    while (i > 0 && heap[(i - 1) / 2]->frequency > heap[i]->frequency) {
        struct SYMBOL* temp = heap[i];
        heap[i] = heap[(i - 1) / 2];
        heap[(i - 1) / 2] = temp;
        i = (i - 1) / 2;
    }
}

void inorder(struct SYMBOL* root) {
    if (root == NULL)
        return;

    inorder(root->left);

    if (root->alphabet != '\0')
        printf("%c  ", root->alphabet);

    inorder(root->right);
}

int main() {
    int n;
    printf("Enter the number of distinct alphabets: ");
    scanf("%d", &n);

    char alphabets[n];
    int frequencies[n];

    printf("Enter the alphabets: ");
    for (int i = 0; i < n; i++)
        scanf(" %c", &alphabets[i]);

    printf("Enter its frequencies: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &frequencies[i]);

    struct SYMBOL* heap[n];
    int heapSize = 0;

    for (int i = 0; i < n; i++) {
        heap[heapSize++] = createNode(alphabets[i], frequencies[i]);
    }

    for (int i = heapSize / 2 - 1; i >= 0; i--)
        minHeapify(heap, heapSize, i);

    while (heapSize > 1) {
        struct SYMBOL* left = extractMin(heap, &heapSize);
        struct SYMBOL* right = extractMin(heap, &heapSize);

        struct SYMBOL* internal = createNode('\0', left->frequency + right->frequency);
        internal->left = left;
        internal->right = right;

        insertMinHeap(heap, &heapSize, internal);
    }

    struct SYMBOL* root = extractMin(heap, &heapSize);

    printf("In-order traversal of the tree (Huffman): ");
    inorder(root);
    printf("\n");

    return 0;
}
```

output:

```text
Enter the number of distinct alphabets: 6
Enter the alphabets: a b c d e f
Enter its frequencies: 45 13 12 16 9 5
In-order traversal of the tree (Huffman): a  c  b  f  e  d  
```