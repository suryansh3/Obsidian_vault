---
course: "DAA"
semester: 5
tags:
  - course/daa
up: "[[DAA]]"
---
# Name : Suryansh Mithu
## CSE - 57
## Roll : 24155060


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct person
{
    int id;
    char *name;
    int age;
    int height;
    int weight;
};

void swap(struct person *a, struct person *b)
{
    struct person temp = *a;
    *a = *b;
    *b = temp;
}

void minHeapifyAge(struct person arr[], int n, int i)
{
    int smallest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l].age < arr[smallest].age)
        smallest = l;

    if (r < n && arr[r].age < arr[smallest].age)
        smallest = r;

    if (smallest != i)
    {
        swap(&arr[i], &arr[smallest]);
        minHeapifyAge(arr, n, smallest);
    }
}

void buildMinHeapAge(struct person arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        minHeapifyAge(arr, n, i);
    }
}

void maxHeapifyWeight(struct person arr[], int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l].weight > arr[largest].weight)
        largest = l;

    if (r < n && arr[r].weight > arr[largest].weight)
        largest = r;

    if (largest != i)
    {
        swap(&arr[i], &arr[largest]);
        maxHeapifyWeight(arr, n, largest);
    }
}

void buildMaxHeapWeight(struct person arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        maxHeapifyWeight(arr, n, i);
    }
}

void display(struct person arr[], int n)
{
    printf("Id Name                                  Age                      Height                  Weight(pound)\n");
    for (int i = 0; i < n; i++)
    {
        printf("%-2d %-35s %-24d %-23d %d\n", arr[i].id, arr[i].name, arr[i].age, arr[i].height, arr[i].weight);
    }
}

void insertMinHeap(struct person **arr, int *n)
{
    *arr = (struct person *)realloc(*arr, (*n + 1) * sizeof(struct person));
    struct person new_person;
    new_person.name = (char *)malloc(100 * sizeof(char));
    char fname[50], lname[50];

    printf("Enter Id: ");
    scanf("%d", &new_person.id);
    printf("Enter Name (First and Last): ");
    scanf("%s %s", fname, lname);
    sprintf(new_person.name, "%s %s", fname, lname);
    printf("Enter Age: ");
    scanf("%d", &new_person.age);
    printf("Enter Height: ");
    scanf("%d", &new_person.height);
    printf("Enter Weight: ");
    scanf("%d", &new_person.weight);

    int i = *n;
    (*arr)[i] = new_person;
    (*n)++;

    while (i > 0 && (*arr)[(i - 1) / 2].age > (*arr)[i].age)
    {
        swap(&(*arr)[i], &(*arr)[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

void deleteOldest(struct person arr[], int *n)
{
    if (*n <= 0)
    {
        printf("Heap is empty.\n");
        return;
    }
    int max_idx = 0;
    for (int i = 1; i < *n; i++)
    {
        if (arr[i].age > arr[max_idx].age)
        {
            max_idx = i;
        }
    }
    free(arr[max_idx].name);
    arr[max_idx] = arr[*n - 1];
    (*n)--;
    buildMinHeapAge(arr, *n);
}

int main()
{
    struct person *students = NULL;
    int n = 0;
    int choice;

    while (1)
    {
        printf("MAIN MENU (HEAP)\n");
        printf("1. Read Data\n");
        printf("2. Create a Min-heap based on the age\n");
        printf("3. Create a Max-heap based on the weight\n");
        printf("4. Display weight of the youngest person\n");
        printf("5. Insert a new person into the Min-heap\n");
        printf("6. Delete the oldest person\n");
        printf("7. Exit\n\n");
        printf("Enter option: ");
        if (scanf("%d", &choice) != 1)
            break;

        switch (choice)
        {
        case 1:
        {
            FILE *fp = fopen("Student.txt", "r");
            if (!fp)
                fp = fopen("student.txt", "r");
            if (!fp)
            {
                printf("Error opening file \n");
                break;
            }
            if (students != NULL)
            {
                for (int i = 0; i < n; i++)
                    free(students[i].name);
                free(students);
                students = NULL;
            }
            n = 0;
            char fname[50], lname[50];
            int id, age, height, weight;
            while (fscanf(fp, "%d %s %s %d %d %d", &id, fname, lname, &age, &height, &weight) == 6)
            {
                n++;
            }
            rewind(fp);
            students = (struct person *)malloc(n * sizeof(struct person));
            for (int i = 0; i < n; i++)
            {
                fscanf(fp, "%d %s %s %d %d %d", &students[i].id, fname, lname, &students[i].age, &students[i].height, &students[i].weight);
                students[i].name = (char *)malloc(100 * sizeof(char));
                sprintf(students[i].name, "%s %s", fname, lname);
            }
            fclose(fp);
            display(students, n);
            break;
        }
        case 2:
            if (n > 0)
            {
                buildMinHeapAge(students, n);
                display(students, n);
            }
            else
            {
                printf("No data available.\n");
            }
            break;
        case 3:
            if (n > 0)
            {
                buildMaxHeapWeight(students, n);
                display(students, n);
            }
            else
            {
                printf("No data available.\n");
            }
            break;
        case 4:
            if (n > 0)
            {
                buildMinHeapAge(students, n);
                printf("Weight of youngest student: %d pound\n", students[0].weight);
            }
            else
            {
                printf("No data available.\n");
            }
            break;
        case 5:
            insertMinHeap(&students, &n);
            break;
        case 6:
            if (n > 0)
            {
                deleteOldest(students, &n);
            }
            else
            {
                printf("Heap is empty.\n");
            }
            break;
        case 7:
            if (students != NULL)
            {
                for (int i = 0; i < n; i++)
                    free(students[i].name);
                free(students);
            }
            return 0;
        default:
            printf("Invalid option!\n");
        }
    }
    return 0;
}
```


```Student.txt
0 Adarsh Hota 39 77 231
1 Levi Maier 56 77 129
2 Priya Kumari 63 78 240
3 Dorothy Helton 47 72 229
4 Florence Smith 24 75 171
5 Erica Anyan 38 73 102
6 Norma Webster 23 75 145
```




``` txt
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Id Name                                  Age                      Height                  Weight(pound)
0  Adarsh Hota                         39                       77                      231
1  Levi Maier                          56                       77                      129
2  Priya Kumari                        63                       78                      240
3  Dorothy Helton                      47                       72                      229
4  Florence Smith                      24                       75                      171
5  Erica Anyan                         38                       73                      102
6  Norma Webster                       23                       75                      145
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Id Name                                  Age                      Height                  Weight(pound)
6  Norma Webster                       23                       75                      145
4  Florence Smith                      24                       75                      171
5  Erica Anyan                         38                       73                      102
3  Dorothy Helton                      47                       72                      229
1  Levi Maier                          56                       77                      129
0  Adarsh Hota                         39                       77                      231
2  Priya Kumari                        63                       78                      240
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Weight of youngest student: 145 pound
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Id Name                                  Age                      Height                  Weight(pound)
2  Priya Kumari                        63                       78                      240
3  Dorothy Helton                      47                       72                      229
0  Adarsh Hota                         39                       77                      231
4  Florence Smith                      24                       75                      171
1  Levi Maier                          56                       77                      129
6  Norma Webster                       23                       75                      145
5  Erica Anyan                         38                       73                      102
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Enter Id: Enter Name (First and Last): Enter Age: Enter Height: Enter Weight: MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: Weight of youngest student: 135 pound
MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: MAIN MENU (HEAP)
1. Read Data
2. Create a Min-heap based on the age
3. Create a Max-heap based on the weight
4. Display weight of the youngest person
5. Insert a new person into the Min-heap
6. Delete the oldest person
7. Exit

Enter option: 
```

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[DAA]] · **Semester:** [[Semester 5]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Semester 5/DAA/Lab/Day3|Day3]] · **Next:** [[04 - Academics & CS/Semester 5/DAA/Lab/day8|day8]]
> **Related:** [[Data Structures]] · [[Discrete Mathematics]] · [[OOPJ (Java)]]
<!-- connections:end -->
