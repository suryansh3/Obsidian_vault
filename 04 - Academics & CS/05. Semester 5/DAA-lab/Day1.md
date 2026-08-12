## 1.1

```c
#include <stdio.h>
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i,a[100],s1,s2,l1,l2;
f=fopen("in.txt","r");
fscanf(f,"%d",&n);
for(i=0;i<n;i++) fscanf(f,"%d",&a[i]);
fclose(f);
s1=s2=999999;
l1=l2=-999999;
for(i=0;i<n;i++){
if(a[i]<s1){s2=s1;s1=a[i];}
else if(a[i]<s2 && a[i]!=s1) s2=a[i];
if(a[i]>l1){l2=l1;l1=a[i];}
else if(a[i]>l2 && a[i]!=l1) l2=a[i];
}
printf("Second smallest = %d\nSecond largest = %d\n",s2,l2);
return 0;
}
```

```
6
12 45 9 32 7 18
```

```
$ gcc day1.1.c -o day1.1
$ ./day1.1
Name : Suryansh Mithu
Roll : 24155060
Second smallest = 9
Second largest = 32
```

---
## 1.2

```c
#include <stdio.h>
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i,a[100],p[100];
f=fopen("in.txt","r");
fscanf(f,"%d",&n);
for(i=0;i<n;i++) fscanf(f,"%d",&a[i]);
fclose(f);
p[0]=a[0];
for(i=1;i<n;i++) p[i]=p[i-1]+a[i];
printf("Prefix Sum: ");
for(i=0;i<n;i++) printf("%d ",p[i]);
printf("\n");
return 0;
}
```

```
5
3 4 5 1 2
```

```
$ gcc day1.2.c -o day1.2
$ ./day1.2
Name : Suryansh Mithu
Roll : 24155060
Prefix Sum: 3 7 12 13 15
```

---
## 1.3

```c
#include <stdio.h>
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i,j,k,a[100],dup=0,most,freq,maxf=0;
printf("Enter how many numbers you want to read from file: ");
scanf("%d",&n);
f=fopen("in.txt","r");
for(i=0;i<n;i++) fscanf(f,"%d",&a[i]);
fclose(f);
printf("The content of the array: ");
for(i=0;i<n;i++) printf("%d ",a[i]);
printf("\n");
for(i=0;i<n;i++){
int c=1;
if(a[i]==-1) continue;
for(j=i+1;j<n;j++) if(a[j]==a[i]){c++;a[j]=-1;}
if(c>1) dup++;
if(c>maxf){maxf=c;most=a[i];}
}
printf("Total number of duplicate values = %d\n",dup);
printf("The most repeating element in the array = %d\n",most);
return 0;
}
```

```
10 40 35 47 68 22 40 10 98 10 50 35 68 40 10
```

**Terminal run**
```
$ gcc day1.3.c -o day1.3
$ ./day1.3
Name : Suryansh Mithu
Roll : 24155060
Enter how many numbers you want to read from file: 15
The content of the array: 10 40 35 47 68 22 40 10 98 10 50 35 68 40 10 
Total number of duplicate values = 4
The most repeating element in the array = 10
```

---

## 1.4

```c
#include <stdio.h>
void exchange(int *p,int *q){int t=*p;*p=*q;*q=t;}
void rotate_right(int p1[],int p2){
int i;
for(i=p2-1;i>0;i--) exchange(&p1[i],&p1[i-1]);
}
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
int n,i,a[100];
printf("Enter an array A of size N (9): ");
scanf("%d",&n);
for(i=0;i<n;i++) scanf("%d",&a[i]);
printf("Before ROTATE: ");
for(i=0;i<n;i++) printf("%d ",a[i]);
rotate_right(a,5);
printf("After   ROTATE: ");
for(i=0;i<n;i++) printf("%d ",a[i]);
printf("\n");
return 0;
}
```


```
$ gcc day1.4.c -o day1.4
$ ./day1.4
Name : Suryansh Mithu
Roll : 24155060
Enter an array A of size N (9): 9
11 22 33 44 55 66 77 88 99
Before ROTATE: 11 22 33 44 55 66 77 88 99 
After   ROTATE: 55 11 22 33 44 66 77 88 99 
```

---

## 1.5

```c
#include <stdio.h>
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *in,*out;
int n,q,i,l,r,a[100],p[100];
in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%d",&n);
for(i=0;i<n;i++) fscanf(in,"%d",&a[i]);
fscanf(in,"%d",&q);
p[0]=a[0];
for(i=1;i<n;i++) p[i]=p[i-1]+a[i];
fprintf(out,"Prefix Sum: ");
for(i=0;i<n;i++) fprintf(out,"%d ",p[i]);
fprintf(out,"\n");
for(i=0;i<q;i++){
fscanf(in,"%d %d",&l,&r);
int sum=p[r]-(l>0?p[l-1]:0);
fprintf(out,"Range Sum (%d,%d) = %d\n",l,r,sum);
}
fclose(in);fclose(out);
printf("Results written to out.txt\n");
return 0;
}
```

```
5
2 4 6 8 10
3
1 3
0 4
2 2
```

```
$ gcc day1.5.c -o day1.5
$ ./day1.5
Name : Suryansh Mithu
Roll : 24155060
Results written to out.txt
```

**Output file**
```
Prefix Sum: 2 6 12 20 30 
Range Sum (1,3) = 18
Range Sum (0,4) = 30
Range Sum (2,2) = 6
```

---

## 1.6 – Equilibrium Index

**Code (`day1.6.c`)**

```c
#include <stdio.h>
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *f;
int n,i,a[100],total=0,left=0,found=0;
f=fopen("in.txt","r");
fscanf(f,"%d",&n);
for(i=0;i<n;i++){fscanf(f,"%d",&a[i]);total+=a[i];}
fclose(f);
for(i=0;i<n;i++){
total-=a[i];
if(left==total){printf("Equilibrium Index = %d\n",i);found=1;}
left+=a[i];
}
if(!found) printf("No equilibrium index exists.\n");
return 0;
}
```


```
5
1 3 5 2 2
```

```
$ gcc day1.6.c -o day1.6
$ ./day1.6
Name : Suryansh Mithu
Roll : 24155060
Equilibrium Index = 2
```

---

## 1.7


```c
#include <stdio.h>
void exchange(int *p,int *q){int t=*p;*p=*q;*q=t;}
void reverse(int a[],int s,int e){
while(s<e){exchange(&a[s],&a[e]);s++;e--;}
}
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *in,*out;
int n,k,i,a[100];
in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%d",&n);
for(i=0;i<n;i++) fscanf(in,"%d",&a[i]);
fscanf(in,"%d",&k);
k=k%n;
fprintf(out,"Before rotation: ");
for(i=0;i<n;i++) fprintf(out,"%d ",a[i]);
reverse(a,0,k-1);
reverse(a,k,n-1);
reverse(a,0,n-1);
fprintf(out,"\nAfter rotation:  ");
for(i=0;i<n;i++) fprintf(out,"%d ",a[i]);
fprintf(out,"\n");
fclose(in);fclose(out);
printf("Result written to out.txt\n");
return 0;
}
```

```
6
1 2 3 4 5 6
2
```

```
$ gcc day1.7.c -o day1.7
$ ./day1.7
Name : Suryansh Mithu
Roll : 24155060
Result written to out.txt
```

**Output file `out.txt`**
```
Before rotation: 1 2 3 4 5 6 
After rotation:  3 4 5 6 1 2 
```

---

## 1.8

```c
#include <stdio.h>
void exchange(int *p,int *q){int t=*p;*p=*q;*q=t;}
void rotate_right(int a[],int n){
int i;
for(i=n-1;i>0;i--) exchange(&a[i],&a[i-1]);
}
int main()
{
printf("Name : Suryansh Mithu\nRoll : 24155060\n");
FILE *in,*out;
int n,k,i,a[100];
in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%d",&n);
for(i=0;i<n;i++) fscanf(in,"%d",&a[i]);
fscanf(in,"%d",&k);
k=k%n;
for(i=0;i<k;i++) rotate_right(a,n);
fprintf(out,"After right rotation: ");
for(i=0;i<n;i++) fprintf(out,"%d ",a[i]);
fprintf(out,"\n");
fclose(in);fclose(out);
printf("Result written to out.txt\n");
return 0;
}
```

```
5
10 20 30 40 50
3
```

```
$ gcc day1.8.c -o day1.8
$ ./day1.8
Name : Suryansh Mithu
Roll : 24155060
Result written to out.txt
```

Output file
```
After right rotation: 30 40 50 10 20 
```

